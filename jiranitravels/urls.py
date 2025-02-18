from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('places/',include('destinations.urls')),
    # path('destinations/',include('destinations.urls')),
=======
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
>>>>>>> Wambo-Dev
]
