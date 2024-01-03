from rest_framework.permissions import *


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if 'admin' in request.user.username:
            return True
        elif request.method in SAFE_METHODS:
            return True
