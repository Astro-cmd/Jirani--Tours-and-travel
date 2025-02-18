from . models import Destinations, Tours
from rest_framework import serializers
class DestinationSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = ['name','location','country','address','images']
    
class ToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = ['package_id', 'destination_id', 'price', 'start_date', 'end_date', 'available_slots' ]
