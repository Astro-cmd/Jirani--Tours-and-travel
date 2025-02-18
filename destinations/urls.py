from django.urls import path
from .views import DestinationsView
urlpatterns = [
    path('destinations/',DestinationsView.as_view(), name = 'new_destinations')
]