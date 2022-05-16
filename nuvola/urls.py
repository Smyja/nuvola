from django.contrib import admin
from django.urls import path
from core.views import flight_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/flights/", flight_list),
]
