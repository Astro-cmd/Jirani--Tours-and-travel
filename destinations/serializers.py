from . models import Destinations
from rest_framework import serializers
class DestinationSerialiazer(serializers.Serializer):
    model = Destinations
    fields = ['name','location','country','address']
    
