from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Flight
from django.db.models import Q
from .serializers import FlightSerializer, FlightUpdateSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method="PUT",
    request_body=FlightUpdateSerializer,
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

    if request.method == "PUT":
        serializer = FlightUpdateSerializer(flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# create flight
@swagger_auto_schema(
    method="POST",
    request_body=FlightSerializer,
    operation_description="Create flight",
)
@api_view(["POST"])
def flight_create(request):
    if request.method == "POST":
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete flight
@swagger_auto_schema(
    method="DELETE",
    operation_description="Delete flight",
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
@api_view(["DELETE"])
def flight_delete(request, flight_number):
    try:
        flight = Flight.objects.get(flight_number=flight_number)
    except Flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Get flight list by origin and destination, departure time and arrival time
@swagger_auto_schema(
    method="GET",
    operation_description="Returns a list of all flights between departure time or arrival time or origin and destination",
    manual_parameters=[
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
    ],
)
@api_view(["GET"])
def flight_list(request):
    origin = request.GET.get("origin")
    destination = request.GET.get("destination")
    departure_time = request.GET.get("departure_time")
    arrival_time = request.GET.get("arrival_time")
    if origin or destination or departure_time or arrival_time:
        flights = Flight.objects.filter(
            Q(origin=origin) | Q(destination=destination) |Q( # noqa: E711
                Q(departure_time=departure_time) | Q(arrival_time=arrival_time)
            )
        )
    else:
        flights = Flight.objects.all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)

