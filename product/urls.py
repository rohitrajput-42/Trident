from django.urls import path
from .views import Product_list

urlpatterns = [
    path('product_list', Product_list.as_view(), name = "product_list")
]