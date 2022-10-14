from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude= ['groups', 'user_permissions', 'last_login', 'is_active', 'is_staff', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data: dict) -> dict:
        account = Account.objects.create_user(**validated_data)
        
        return account
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)