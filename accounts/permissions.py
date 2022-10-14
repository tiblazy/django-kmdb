from rest_framework import permissions
from rest_framework.views import Request

class AccountPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, _, obj: object) -> bool:
        return (request.user.is_superuser or obj == request.user and request.user.is_critic)