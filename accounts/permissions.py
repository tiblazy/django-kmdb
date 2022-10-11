from rest_framework import permissions

class AccountPermission(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        if request.method == 'GET':
            
            if request.user.is_authenticated and request.user.is_superuser:
                return True
            
            if request.user.is_authenticated and request.user.is_critic:
                return obj == request.user
        
            return False
        return False            