from django.urls import path, include
from .views import InventoryListView, InventoryUpdateView, CategoryListView, CategoryUpdateView


urlpatterns = [
    path('', InventoryListView.as_view()),
    path('inventory/<int:pk>/', InventoryUpdateView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryUpdateView.as_view())

]