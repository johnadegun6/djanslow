# from django.shortcuts import render
# from django.urls import path
# from core.views import index
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# urlpatterns = [
#     path('', view)
# ]

def index_view(request):
    return Response({'status':status.HTTP_200_OK})