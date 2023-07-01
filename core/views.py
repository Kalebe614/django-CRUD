from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductModel

class ProductListView(ListView):
    model = ProductModel
    template_name = 'product_list.html'
    queryset = ProductModel.objects.all()
    context_object_name = "products"