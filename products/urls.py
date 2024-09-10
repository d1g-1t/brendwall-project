from django.urls import path
from .views import index, ProductListCreate

urlpatterns = [
    path('', index, name='index'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
]