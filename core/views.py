from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Flight, Aircraft
from .serializers import FlightSerializer, AircraftSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# list of departure airports and arrival airports of all flights between departure time and arrival time

@swagger_auto_schema(
    method="GET",
    operation_description="Returns a list of all flights between departure time and arrival time",
    manual_parameters=[
        openapi.Parameter(
            "departure_time",
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Departure time in format YYYY-MM-DD HH:MM:SS",
            required=True,
        ),
        openapi.Parameter(
            "arrival_time",
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Arrival time in format YYYY-MM-DD HH:MM:SS",
            required=True,
        ),
    ],
)
@api_view(["GET"])
def flight_list(request):
    departure_time = request.GET.get("departure_time")
    arrival_time = request.GET.get("arrival_time")
    flights = Flight.objects.filter(
        departure_time__range=(departure_time, arrival_time)
    )
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


# list of all flights
