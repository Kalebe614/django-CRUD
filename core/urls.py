from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', ProductListView.as_view(), name='product_list'),
   path('create/', ProductCreateView.as_view(), name='product_create'),
   path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)