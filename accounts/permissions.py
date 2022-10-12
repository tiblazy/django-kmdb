from rest_framework import permissions

class AccountPermission(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        if request.method == 'GET':
            if request.user.is_authenticated:
                
                if request.user.is_superuser or obj == request.user and request.user.is_critic:
                    return True
                        
                return False
            return False
        return False    