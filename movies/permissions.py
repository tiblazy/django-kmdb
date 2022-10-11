from rest_framework import permissions

class MoviePermission(permissions.BasePermission):
    def has_permission(self, request, _):
        if not request.method == 'GET':
            if request.user.is_authenticated and request.user.is_superuser:
                return True
            
            return False    
        return True