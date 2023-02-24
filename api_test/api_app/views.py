from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Products_Collection,Carts,User,Cart
from .serializers import ProductsSerializer,CartsSerializer,CartSerializer,VariantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from django.urls import reverse
from django.db.models import Q


# Create your views here.
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        prod=Products_Collection.objects.all()
        serial=ProductsSerializer(prod,many=True)
        return Response(serial.data,safe=False)

    if request.method == 'POST':
        data = request.data
        serializer = ProductsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()   
            return Response('Posted')
@api_view(['GET', 'POST'])
def showcart(request,data):
    if request.method == 'GET':
        prods=Cart.objects.filter(name=data)
        serial=CartSerializer(prods,many=True)
        # return redirect(url)
        return Response(serial.data)

    if request.method == 'POST':
        serializer = CartSerializer(request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response('Posted')
@api_view(['GET'])
def variant(request,slug,id):
    if request.method == 'GET':
        product=Products_Collection.objects.get(Q(product_slug=slug) & Q(id=id))
        serial=VariantSerializer(product)
        return Response(serial.data)


# @api_view(['GET', 'POST'])
# def usher(request):
#       if request.method == 'GET':
#         serial=UserSerializer(request.user)
#         print(serial)
#         print(serial.data)
#         return JsonResponse(serial.data)      
