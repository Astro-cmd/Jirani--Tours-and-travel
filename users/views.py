from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, UserProfile
from .serializers import CustomUserSerializer, UserProfileSerializer
import logging

logger = logging.getLogger(__name__)
# Create your views here.
# List & Create Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
# validate if the user exist

    def create (self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            return Response({"error": "An error occured while creating the user."}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    


# Retrieve, Update & Delete User
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

# List & Create User Profiles
class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Retrieve, Update & Delete User Profile
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
