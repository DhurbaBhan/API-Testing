from rest_framework import serializers
from .models import Products_Collection

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products_Collection
        fields="__all__"

# image=serializers.ImageField(upload_to='images')
# vendor=serializers.CharField(max_length=100)
# product_title=serializers.CharField(max_length=100)
# rating=serializers.PositiveIntegerField()
# price=serializers.FloatField()