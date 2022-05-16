from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from news.models import Stories
from .serializers import StoriesSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

