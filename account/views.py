from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from .models import User


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProfile(RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
