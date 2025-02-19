from django.urls import path
from .views import DestinationsView, ToursView
urlpatterns = [
    path('destinations/',DestinationsView.as_view(), name = 'new_destinations'),
    path('tours/', ToursView.as_view(), name = 'tour packages')
]