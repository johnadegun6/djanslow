# from django.shortcuts import render
# from django.urls import path
# from core.views import index
from rest_framework.response import Response
from rest_framework import status
from core.models import Customer
from core.serializer import CustomerSerializer
# Create your views here.

# urlpatterns = [
#     path('', view)
# ]

def index_view(request):
    return Response({'status':status.HTTP_200_OK})


def add_customer(request):
    data = request.data
    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':status.HTTP_201_CREATED})