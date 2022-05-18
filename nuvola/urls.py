from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from django.urls import path
from core.views import flight_list, flight_update, flight_create, flight_delete

schema_view = get_schema_view(
    openapi.Info(
        title="Fleet Management Api",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/flights/", flight_list),
    path("api/v1/flights/<int:flight_number>/", flight_update),
    path("api/v1/create/", flight_create),
    path("api/v1/delete/<str:flight_number>/", flight_delete),
    path(
        "api/v1/docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
