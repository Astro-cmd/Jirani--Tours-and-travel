from django.db import models
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

    # extract the latitude, longitude coordinates from plaintextfield

    # def save(self,*args, **kwargs):
    #     if self.location:
    #         lat,lng = self.location.split(',')
    #         self.latitude = float(lat)
    #         self.longitude = float(lng)

    #     super().save(*args, **kwargs)

    # def __str__(self):
        # return f"{self.name} - {self.latitude}, {self.longitude}"

