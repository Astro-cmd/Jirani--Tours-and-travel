from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from shortuuid.django_fields import ShortUUIDField
import string
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from django.apps import apps


ROLES = [('tourist', 'Tourist'),
         ('admin', 'Admin'),
         ('guide', 'Guide'),]

# Create your models here.
class  CustomUser (AbstractUser):
    user_id = ShortUUIDField(unique = True, length = 10, max_length= 15, alphabet = string.digits)
    first_name = models.CharField(max_length= 15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique = True, null=False, blank=False)
    password_hash = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now= True)
    role = models.CharField(max_length= 15, choices=ROLES, default= 'tourist')
    profile_picture = models.ImageField(height_field = 100, upload_to='media/profiles', blank=True,null=True)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name,self.role}( {self.role})"
    

    
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLES)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)  # Fixed ForeignKey

    def __str__(self):
        return self.name



