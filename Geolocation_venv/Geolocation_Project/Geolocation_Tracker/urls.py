from django.urls import path
from . import views

urlpatterns = [
    path('',views.Geolocation_Tracker,name='Geolocation_Tracker')
]