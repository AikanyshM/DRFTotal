from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class BasicPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True

