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
        account = Account.objects.create(**validated_data)
        
        return account
    
    
# fazer depois
# Customize o Django Admin para estar 100% funcional com o usuário customizado.