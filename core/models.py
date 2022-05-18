import django
from django.utils import timezone
from datetime import datetime
import uuid
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


class Flight(models.Model):
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    flight_number = models.CharField(max_length=5)
    departure_time = models.DateTimeField(default=django.utils.timezone.now)
    arrival_time = models.DateTimeField()
    aircraft = models.ForeignKey("Aircraft", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Last updated", auto_now=True)

    class Meta:
        verbose_name_plural = "Flights"
        ordering = ("departure_time",)

    def clean(self):
        if self.departure_time < timezone.now():
            raise ValidationError("Departure time must be in the future")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.flight_number


class Aircraft(models.Model):
    serial_number = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
    )
    manufacturer = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Aircrafts"

    def __str__(self):
        return self.manufacturer
