from .models import Flight, Aircraft
from rest_framework import serializers


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            "origin",
            "destination",
            "flight_number",
            "departure_time",
            "arrival_time",
            "aircraft",
        )


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ("serial_number", "manufacturer")
