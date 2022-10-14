from rest_framework import permissions
from rest_framework.views import Request

class ReviewPostPermission(permissions.BasePermission):
    def has_permission(self, request: Request, _,) -> bool:
        if request.method == 'POST':
                return (request.user.is_superuser or request.user.is_critic)
        return True            
    
class ReviewDeletePermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, _, obj: object) -> bool:
        if request.method == 'DELETE':
                return (request.user.is_superuser or request.user == obj.critic)
        return True            
    