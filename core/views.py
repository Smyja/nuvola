from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Flight, Aircraft
from .serializers import FlightSerializer, AircraftSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# list of departure airports and arrival airports of all flights between departure time and arrival time and origin and destination

@swagger_auto_schema(
    method="GET",
    operation_description="Returns a list of all flights between departure time and arrival time",
    manual_parameters=[
        openapi.Parameter(
            "departure_time",
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Departure time in format YYYY-MM-DD HH:MM:SS",
            
        ),
        openapi.Parameter(
            "arrival_time",
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Arrival time in format YYYY-MM-DD HH:MM:SS",
            
        ),
        openapi.Parameter(
            "origin",
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Origin airport code",
            
        ),
        openapi.Parameter(
            "destination",
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Destination airport code",
           
        ),
        
    ],
)
@api_view(["GET"])
def flight_list(request):
    origin = request.GET.get("origin")
    destination = request.GET.get("destination")
    departure_time = request.GET.get("departure_time")
    arrival_time = request.GET.get("arrival_time")
    if origin and destination:
        flights = Flight.objects.filter(
            origin=origin, destination=destination
        ).order_by("departure_time")
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    else:
        flights = Flight.objects.filter(
            departure_time__range=[departure_time, arrival_time]
        ).order_by("departure_time")
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)


# Update flight details
@swagger_auto_schema(
    method="PUT",
    request_body=FlightSerializer,
    operation_description="Update flight details",
    manual_parameters=[
        openapi.Parameter(
            "flight_number",
            in_=openapi.IN_PATH,
            type=openapi.TYPE_STRING,
            description="Flight number",
            required=True,
        ),
    ],
)
@api_view(["PUT"])
def flight_update(request, flight_number):
    try:
        flight = Flight.objects.get(flight_number=flight_number)
    except Flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FlightSerializer(flight, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

