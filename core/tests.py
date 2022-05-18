
import json
from datetime import datetime
from django.utils import timezone
from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from requests import request
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from core.models import Flight, Aircraft
from .views import flight_list, flight_update, flight_create, flight_delete

# Create your tests here.


class FlightTestCase(TestCase):
    def setUp(self):
        self.client1 = APIRequestFactory()
        self.client = APIClient()

        self.flight = Flight.objects.create(
            origin="LHR",
            destination="JFK",
            departure_time=timezone.make_aware(
                datetime.strptime("01/01/2025 00:00 UTC", "%d/%m/%Y %H:%M %Z"),
                timezone.get_default_timezone(),
            ),
            arrival_time=timezone.make_aware(
                datetime.strptime("2026-01-01T00:00:00", "%Y-%m-%dT%H:%M:%S"),
                timezone.get_current_timezone(),
            ),
            aircraft=Aircraft.objects.create(manufacturer="AirPeace A320"),
            flight_number="BA123",
        )

        self.aircraft_id = Aircraft.objects.get(manufacturer="AirPeace A320").id

    def test_flight_create(self):

        response = self.client.post(
            "/api/v1/create/",
            {
                "origin": "LHR",
                "destination": "JFK",
                "departure_time": "2025-01-01T00:00:00Z",
                "arrival_time": "2026-01-01T00:00:00Z",
                "aircraft": Aircraft.objects.create(manufacturer="Airbus A320").id,
                "flight_number": "BA123",
            },
        )
        print(response.json())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {
                "origin": "LHR",
                "destination": "JFK",
                "departure_time": "2025-01-01T00:00:00Z",
                "arrival_time": "2026-01-01T00:00:00Z",
                "aircraft": Aircraft.objects.get(manufacturer="Airbus A320").id,
                "flight_number": "BA123",
            },
        )

    def test_flight_list(self):
        response = self.client.get("/api/v1/flights/")
        self.assertEqual(response.status_code, 200)
        print(response.json(), "test_flight_list")
        self.assertEqual(
            response.json(),
            [
                {
                    "origin": "LHR",
                    "destination": "JFK",
                    "departure_time": "2025-01-01T00:00:00Z",
                    "arrival_time": "2026-01-01T00:00:00Z",
                    "aircraft": self.aircraft_id,
                    "flight_number": "BA123",
                }
            ],
        )

    def test_flight_update(self):
        request = self.client1.put("/api/v1/flights/BA123/", {"origin": "HR"}, format="json")
        response = flight_update(request, "BA123")
        response.render()
        print(response.rendered_content, "test_flight_update")
        self.assertEqual(response.status_code, 200)
        # print(response.content.json(), "test_flight_update")


    def test_flight_delete(self):

        request = self.client1.delete("/api/v1/delete/BA123/")
        response = flight_delete(request, "BA123")
        response.render()
        print(response.rendered_content, "test_flight_delete")
        self.assertEqual(response.status_code, 204)
        
        self.assertEqual(response.content, b"")
    
    
