from django.contrib import admin
from .models import ProductModel
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','id','description','price', 'image', 'created', 'updated']
