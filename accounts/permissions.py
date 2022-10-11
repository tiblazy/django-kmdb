from rest_framework import permissions

class AccountPermission(permissions.BasePermission):
    def has_permission(self, request, _):
        if request.method == 'GET':
            print(request)
            print(request.GET)
            print(request.GET.get('id'))
            print(request.auth)
            if request.user.is_authenticated and request.user.is_superuser:
                return True
            
            if request.user.is_authenticated and request.user.is_critic:
                return True
            
            return False
        return False
    
class AccountMoviePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.method == 'DELETE':
            if request.user.is_authenticated and request.user.is_superuser:
                return True
            
            return False    
        return True