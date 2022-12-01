from django.shortcuts import render
from django.http import JsonResponse
from .models import Products_Collection
from .serializers import ProductsSerializer

# Create your views here.
def products(request):
    prod=Products_Collection.objects.all()
    serial=ProductsSerializer(prod,many=True)
    return JsonResponse(serial.data,safe=False)