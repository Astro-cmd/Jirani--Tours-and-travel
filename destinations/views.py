from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response


# Create your views here.
class DestinationsView(APIView):
     def get(self, request):
          queryset = Destinations.objects.all()
          serializer =  DestinationSerialiazer(queryset, many = True)

          output = {
               'message' : 'all destinations are listed',
               'result' : serializer.data
          }

          return Response(output, status= status.HTTP_200_OK)
     def post(self,request):
          serializer = DestinationSerialiazer(data = request.data)
          input_data = request.data
          new_detinations  = Destinations.objects.create(**input_data)

          try: 
            serializer.is_valid(raise_exception=True)

            serializer.save()
            return Response(
                {
                    'message' : 'destinations created successfully',
                    'result' : serializer.data
                    
                }, status=status.HTTP_201_CREATED
            )
          except ValidationError as e:
            # handle validation errors

            return Response({
                'message': "an error occured while adding destination",
                'errors':str(e)

            }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
          
          return Response ('Added destination', status = status.HTTP_201_CREATED)
        
            
          
class ToursView(APIView):
    def get(self, request):
        queryset = Tours.objects.all()
        serializer = ToursSerializer(queryset, many = True)

        data = {
            'message' : 'succesfully got all available tours',
            'result' : serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ToursSerializer(data = request.data)
        input_data = request.data
        new_tours = Tours.objects.create(**input_data)

        'handling of validation errors that occur during data input'
        try:
             serializer.is_valid(raise_exception=True)
             serializer.save()
             return Response(
                 {
                     'message' : 'tours added successfully',
                     'result' : serializer.data
                 }, status=status.HTTP_201_CREATED
             )
        except ValidationError as e:
            return Response(
                {
                    'message' : 'an error occured while adding tour packages',
                    'errors': str(e)
                 }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response('tours added', status=status.HTTP_201_CREATED)

