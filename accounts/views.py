from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth import authenticate

from .models import Account
from .serializers import AccountSerializer, LoginSerializer

class AccountRegisterView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def perform_create(self, serializer):
        return serializer.save()
    
class AccountLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        account = authenticate(**serializer.validated_data)
        
        if account:
            token, _ = Token.objects.get_or_create(user=account)
            return Response({
                'token': token.key,
            })

        return Response({'detail': 'invalid username or password'}, status.HTTP_400_BAD_REQUEST)
