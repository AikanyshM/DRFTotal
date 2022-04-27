from django.shortcuts import render
from .models import Inventory, Category
from .serializers import InventorySerializer, CategorySerializer
from rest_framework import authentication
from rest_framework import permissions
from .permissions import BasicPermission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from account.models import User


class InventoryListView(ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [BasicPermission, ]

    def check_seller(self, request, name, cost, seller, category):
        if request.user == User.seller:
            new_inventory = Inventory.objects.create(name=name, cost=cost, seller=seller, category=category)
            return new_inventory
        return Response({"error": "You are not allowed to add new items unless you're a seller"})


class InventoryUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

class CategoryListView(ListCreateAPIView):
    categories = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def check_buyer(self, request):
        if request.user == User.buyer:
            categories = Category.objects.all()
            return categories
        return Response({"error": "You are not allowed to see all categories unless you're a buyer"})

    def add_category(self, request, name):
        if request.user.is_superuser:
            new_cat = Category.objects.create(name=name)
            return new_cat
        return Response({"error": "You are not allowed to add new categories unless you're a superuser"})


class CategoryUpdateView(RetrieveUpdateDestroyAPIView):
    categories = Category.objects.all()
    serializer_class = CategorySerializer(categories, many=True)
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    