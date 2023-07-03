from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import ProductModel
from .forms import ProductModelForm
from django.contrib import messages
from django.core.paginator import Paginator


class ProductListView(ListView):
    model = ProductModel
    template_name = 'product_list.html'
    queryset = ProductModel.objects.all().filter(activity=True).order_by('-id')
    context_object_name = "products"
    paginate_by = 2

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

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Product deleted successfully')
        return response
    
class ProductUpdateView(UpdateView):
    model = ProductModel
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')
    form_class = ProductModelForm

    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request, 'Product updated successfully')
        return response

class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product_detail.html'
    