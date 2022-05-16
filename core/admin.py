from django.contrib import admin

# Register your models here.
from .models import Flight, Aircraft


class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "origin",
        "destination",
        "flight_number",
        "departure_time",
        "arrival_time",
        "aircraft",
    )
    list_filter = ("departure_time", "arrival_time")
    raw_id_fields = ["aircraft"]
    search_fields = ("origin", "destination", "flight_number")


class AircraftAdmin(admin.ModelAdmin):
    list_display = ("manufacturer","serial_number")
    search_fields = ("serial_number", "manufacturer")

class FlightInline(admin.TabularInline):
    model = Flight
    extra = 1


admin.site.register(Flight, FlightAdmin)
admin.site.register(Aircraft, AircraftAdmin)
