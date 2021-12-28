
from django.urls import path
from .views import  send_mesage


urlpatterns = [
    path('send/', send_mesage),
   
]