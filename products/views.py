from rest_framework import viewsets, serializers, generics, filters
from rest_framework.response import Response

from products.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'image', 'in_stock', 'weight', 'sold']


class ProductList(generics.ListCreateAPIView):
    search_fields = ['name']
    model = Product
    filter_backends = (filters.SearchFilter,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
