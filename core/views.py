from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import ProductModel
from .forms import ProductModelForm
from django.contrib import messages

class ProductListView(ListView):
    model = ProductModel
    template_name = 'product_list.html'
    queryset = ProductModel.objects.all().filter(activity=True)
    context_object_name = "products"

class ProductCreateView(CreateView):
    model = ProductModel
    form_class = ProductModelForm
    template_name= 'product_create.html'
    success_url = reverse_lazy('product_create')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Product created successfully')
        return response

class ProductDeleteView(DeleteView):
    model = ProductModel
    template = 'product_list.html'
    success_url = reverse_lazy('product_list')