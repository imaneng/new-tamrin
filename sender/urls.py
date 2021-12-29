
from django.urls import path
from .views import  delete, create,update


urlpatterns = [
    path('del/<id>', delete),
    path('crt/',create),
    path('update/<int:id>',update)
   
]