from rest_framework import serializers
from .models import Products_Collection,Carts,User,Cart

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products_Collection
        fields=(
            'image',
            'vendor',
            'product_title',
            'rating',
            'price',
        )

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products_Collection
        fields=(
            'image',
            'product_title',
            'weight_in_gm',
            'aroma',
            'appearance',
            'price',

        )

     

class CartsSerializer(serializers.ModelSerializer):
    
    product=SimpleProductSerializer()
    total=serializers.SerializerMethodField(method_name="tot")
    class Meta:
        model=Carts
        fields=(
            'product',
            'quantity', 
            'total', 
        )  

    def tot(self,cart:Carts):
        return cart.quantity*cart.product.price   

class CartSerializer(serializers.ModelSerializer):
    Sub_total=serializers.SerializerMethodField(method_name="subtot")
    items=CartsSerializer(many=True)
    class Meta:
        model=Cart  
        fields=["items","Sub_total"]   

    def subtot(self,cart:Carts):
        items=cart.items.all()
        return sum(item.quantity*item.product.price for item in items)  

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products_Collection
        fields="__all__"               

# class UserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='user.username')
#     class Meta:
#         model=User
#         fields=[
#             "username"
#         ]


