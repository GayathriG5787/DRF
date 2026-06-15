from django.urls import path
from .views import getData, addItem

urlpatterns = [
    path('', getData),
    path('add/', addItem),
]