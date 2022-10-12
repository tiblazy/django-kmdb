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
        validated_data.update({'password': make_password(validated_data['password'])})
        account = Account.objects.create(**validated_data)
        
        return account
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = Account
        fields = ['username', 'password']
    
    def create(self, validated_data):
        account, _ = Account.objects.get_or_create(**validated_data)
        
        return account