from django.urls import path
from . import views

urlpatterns = [
    path('collections/all/',views.products),
    path('cart/',views.showcart),
    # path('product',views.variant),
    path('product/<slug>/<int:id>',views.variant,name="variant"),
   
]