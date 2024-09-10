from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListCreate(generics.ListCreateAPIView):
    """Представление для создания и получения списка продуктов."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        if serializer.validated_data['price'] <= 0:
            raise serializers.ValidationError("Цена должна быть положительным числом")
        serializer.save()


def index(request):
    """Представление для отображения HTML-страницы."""
    return render(request, 'products/index.html')
