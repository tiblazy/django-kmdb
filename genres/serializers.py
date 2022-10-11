from rest_framework import serializers

from .models import Genre

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ['id', 'name']
        # exclude = ['movies']
        
    def create(self, validated_data):
        genre = Genre.objects.get_or_create(**validated_data)
        
        return genre