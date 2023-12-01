from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor, Item
from .serializers import VendorSerializer, ItemSerializer

@api_view(['GET', 'POST'])
def vendor_list(request, format=None):
  if request.method == 'GET':
    vendors = Vendor.objects.all()
    serializer = VendorSerializer(vendors, many = True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def item_list(request, format=None):
  if request.method == 'GET':
    items = Item.objects.all()
    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)