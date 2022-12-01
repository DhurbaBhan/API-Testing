from django.urls import path
from . import views

urlpatterns = [
    path('collections/all',views.products),
   
]