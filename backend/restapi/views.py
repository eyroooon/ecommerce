from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, renderers
from .serializers import *
from .models import *
from .utils import *
import json
import datetime


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by('name')
    serializer_class = ProductSerializer
    

    @action(detail=False)
    def get_cartItems(self, request, pk=None):
        data = cartData(request)
        cartItems = data['cartItems']
        return Response({'cartItem': cartItems})

class CartViewSet(viewsets.ViewSet):

    def list(self, request, pk=None):
        data = cartData(request)    
        items = data['items']
        serializer = OrderItemSerializer(items, many=True)
        

        return Response(serializer.data)
    
