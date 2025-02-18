from django.db import models
from django.db.models import Model
import shortuuid
from location_field.models.plain import PlainLocationField
from shortuuid.django_fields import ShortUUIDField
import string
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from django.apps import apps

# Create your models here.
 
class Destinations(models.Model):
    denstination_id = ShortUUIDField(length = 10,max_length=15,unique=True, alphabet = string.digits)
    name = models.CharField(max_length= 50)
    country = models.CharField(max_length =50)
    address = models.TextField(blank=True, null = True)
    location = PlainLocationField(zoom =7)
    latitude = models.FloatField(editable=False,blank=True,null= True)
    longitude = models.FloatField(editable=False,blank=True,null= True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField( upload_to='media/destinations', blank=True,null=True)

    # extract the latitude, longitude coordinates from plaintextfield

    def save(self,*args, **kwargs):
        if self.location:
            lat,lng = self.location.split(',')
            self.latitude = float(lat)
            self.longitude = float(lng)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.latitude}, {self.longitude}"

class Tours(models.Model):
    tour_id = ShortUUIDField(length = 10 , max_length= 15, unique = True, alphabet = string.digits)
    destination_id = models.ForeignKey(Destinations, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length= 100, null = False, blank = False)
    description = models.TextField(max_length=1000, blank=True , null = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    start_date = models.DateField()
    end_date  = models.DateField()
    available_slots  = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)