from django.db import models

# Create your models here.
class Products_Collection(models.Model):
    image=models.ImageField(upload_to='images')
    vendor=models.CharField(max_length=100)
    product_title=models.CharField(max_length=100)
    rating=models.FloatField()
    price=models.FloatField()

    def __str__(self):
        return self.product_title
