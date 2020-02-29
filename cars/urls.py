from django.contrib import admin
from cars import views
from django.urls import path, include
from .views import CarList


cars_name = 'cars'
urlpatterns = [
    path('', CarList.as_view(), name='carlist'),
]