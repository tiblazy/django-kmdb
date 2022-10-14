from rest_framework import permissions
from rest_framework.views import Request

class MoviePermission(permissions.BasePermission):
    def has_permission(self, request: Request, _) -> bool:
        if not request.method == 'GET':
            return (request.user.is_authenticated and request.user.is_superuser)
        return True