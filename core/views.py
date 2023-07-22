# from django.shortcuts import render
# from django.urls import path
# from core.views import index
from rest_framework.response import Response
from rest_framework import status
from core.models import Customer
from core.serializer import CustomerSerializer
from rest_framework.views import APIView
# Create your views here.

# urlpatterns = [
#     path('', view)
# ]

def index_view(request):
    return Response({'status':status.HTTP_200_OK})


class AddCcustomerView(APIView):
    def post(self, request):
    # name = request.POST.get('name')
    # sex = request.POST.get()
    # data = request.data
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':status.HTTP_201_CREATED})
        return Response({'status':status.HTTP_400_BAD_REQUEST})