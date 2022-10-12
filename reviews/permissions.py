from rest_framework import permissions

class ReviewPostPermission(permissions.BasePermission):
    def has_permission(self, request, _,):
        if request.method == 'POST':
            if request.user.is_authenticated:
                if request.user.is_superuser or request.user.is_critic:
                    return True
                
                return False
            return False
        return True            
    
class ReviewDeletePermission(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        if request.method == 'DELETE':
            if request.user.is_authenticated:
                if request.user.is_superuser or request.user == obj.critic:
                    return True
                
                return False
            return False
        return True            
    