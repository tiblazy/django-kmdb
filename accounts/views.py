from rest_framework.generics import CreateAPIView

from .models import Account
from .serializers import AccountSerializer

class AccountRegisterView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def perform_create(self, serializer):
        return serializer.save()
