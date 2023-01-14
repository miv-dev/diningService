from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from order.models import OrderSerializer, Order


# Create your views here.
class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(OrderSerializer(instance.parent).data)




