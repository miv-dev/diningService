import uuid

from django.db import models
from rest_framework import serializers

from products.models import Product
from products.views import ProductSerializer


# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    group_id = models.CharField(max_length=8, verbose_name="Номер группы")
    first_name = models.CharField(max_length=128, verbose_name="Имя")
    last_name = models.CharField(max_length=128, verbose_name="Фамилия")
    is_ready = models.BooleanField(default=False)
    products = models.ManyToManyField(Product, verbose_name="Продукты")


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'group_id', 'first_name', 'last_name', 'is_ready', 'products']
