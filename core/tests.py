from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Flight, Aircraft

# Create your tests here.


class FlightTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=None)
        Flight.objects.create(
            origin="LHR",
            destination="JFK",
            departure_time="2020-01-01 00:00:00",
            arrival_time="2020-01-01 00:00:00",
            aircraft="A320",
            flight_number="BA123",
        )

    def test_flight_list(self):
        response = self.client.get("/api/v1/flights/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_flight_create(self):
        response = self.client.post(
            "/api/v1/create/",
            {
                "origin": "LHR",
                "destination": "JFK",
                "departure_time": "2020-01-01 00:00:00",
                "arrival_time": "2020-01-01 00:00:00",
                "aircraft": "A320",
                "flight_number": "BA123",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {
                "origin": "LHR",
                "destination": "JFK",
                "departure_time": "2020-01-01 00:00:00",
                "arrival_time": "2020-01-01 00:00:00",
                "aircraft": "A320",
                "flight_number": "BA123",
            },
        )

    def test_flight_update(self):
        response = self.client.put(
            "/api/v1/update/BA123/",
            {
                "origin": "LHR",
                "destination": "JFK",
                "departure_time": "2020-01-01 00:00:00",
                "arrival_time": "2020-01-01 00:00:00",
                "aircraft": "A320",
                "flight_number": "BA123",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "origin": "LHR",
                "destination": "JFK",
                "departure_time": "2020-01-01 00:00:00",
                "arrival_time": "2020-01-01 00:00:00",
                "aircraft": "A320",
                "flight_number": "BA123",
            },
        )

    def test_flight_delete(self):
        response = self.client.delete("/api/v1/delete/BA123/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json(), {})

    def test_flight_list_with_params(self):
        response = self.client.get("/api/v1/flights/?origin=LHR&destination=JFK")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_flight_list_with_params_and_date(self):
        response = self.client.get(
            "/api/v1/flights/?origin=LHR&destination=JFK&departure_time=2020-01-01 00:00:00"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_flight_list_with_params_and_date_range(self):
        response = self.client.get(
            "/api/v1/flights/?origin=LHR&destination=JFK&departure_time=2020-01-01 00:00:00&arrival_time=2020-01-01 00:00:00"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_flight_list_with_params_and_date_range_and_aircraft(self):
        response = self.client.get(
            "/api/v1/flights/?origin=LHR&destination=JFK&departure_time=2020-01-01 00:00:00&arrival_time=2020-01-01 00:00:00&aircraft=A320"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_flight_list_with_params_and_date_range_and_aircraft_and_flight_number(
        self,
    ):
        response = self.client.get(
            "/api/v1/flights/?origin=LHR&destination=JFK&departure_time=2020-01-01 00:00:00&arrival_time=2020-01-01 00:00:00&aircraft=A320&flight_number=BA123"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    # Test Models
    def test_flight_model(self):
        flight = Flight.objects.create(
            origin="LHR",
            destination="JFK",
            departure_time="2020-01-01 00:00:00",
            arrival_time="2020-01-01 00:00:00",
            aircraft="A320",
            flight_number="BA123",
        )
        self.assertEqual(flight.origin, "LHR")
        self.assertEqual(flight.destination, "JFK")
        self.assertEqual(flight.departure_time, "2020-01-01 00:00:00")
        self.assertEqual(flight.arrival_time, "2020-01-01 00:00:00")
        self.assertEqual(flight.aircraft, "A320")
        self.assertEqual(flight.flight_number, "BA123")

    def test_aircraft_model(self):
        aircraft = Aircraft.objects.create(
            aircraft_type="A320", aircraft_model="Airbus A320", aircraft_capacity=100
        )
        self.assertEqual(aircraft.aircraft_type, "A320")
        self.assertEqual(aircraft.aircraft_model, "Airbus A320")
        self.assertEqual(aircraft.aircraft_capacity, 100)
