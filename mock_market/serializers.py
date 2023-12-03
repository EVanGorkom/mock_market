from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vendor
    fields = ['id', 'vendor_name', 'first_name', 'last_name', 'email', 'password']

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    data = {
      "id": representation['id'],
      "type": "vendor",
      "attributes": {
        "vendor_name": representation['vendor_name'],
        "first_name": representation['first_name'],
        "last_name": representation['last_name'],
        "email": representation['email'],
        "password": representation['password'],
      }
    }
    return data #"data": add this out here somehow

class ItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = Item
    fields = ['id', 'item_name', 'vendor', 'price', 'size', 'quantity', 'availability', 'description', 'image']

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    data = {
      "data": {
        "id": representation['id'],
        "type": "item",
        "attributes": {
          "item_name": representation['item_name'],
          "vendor": representation['vendor'],
          "price": representation['price'],
          "size": representation['size'],
          "quantity": representation['quantity'],
          "availability": representation['availability'],
          "description": representation['description'],
          "image": representation['image']
        }
      }
    }
    return data