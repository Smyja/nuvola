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


class FlightUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
        extra_kwargs = {
            "aircraft": {"required": False},
            "departure_time": {"required": False},
            "arrival_time": {"required": False},
            "flight_number": {"required": False},
            "origin": {"required": False},
            "destination": {"required": False},
        }


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ("serial_number", "manufacturer")
