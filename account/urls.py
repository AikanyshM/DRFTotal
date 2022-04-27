from django.urls import path
from .views import UserCreateView, UserProfile

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('profile/', UserProfile.as_view())
]