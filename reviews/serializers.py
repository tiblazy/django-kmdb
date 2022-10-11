from rest_framework import serializers

from .models import Review

from movies.models import Movie
from movies.serializers import MovieSerializer

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ['id', 'stars', 'review', 'spoilers', 'recomendation', 'movie_id', 'critic']
    
    def validate_stars(self, value):
        if type(value)==int and (value>=1 or value<=10):
            return value
        
        raise serializers.ValidationError()
            
    def create(self, validated_data):
        # associar o critico a review
        # associar a review ao filme
        # crítico só pode fazer uma review
        # crítico deve retornar todos os dados do usuário
        
        review = Review.objects.create(**validated_data)
    
        return review
    
    def update(self, instance: Movie, validated_data: dict) -> dict:
        pass
        # if validated_data('genres').exists:
        #     instance.genres.update(**validated_data('genres'))            
                    
        # instance.save()
        
        # return instance