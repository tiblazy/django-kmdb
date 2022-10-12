from rest_framework import serializers

from .models import Movie

from genres.models import Genre
from genres.serializers import GenreSerializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['reviews']
    
    genres = GenreSerializer(many=True)
        
    def create(self, validated_data):
        genre_data = validated_data.pop('genres')
        
        movie = Movie.objects.create(**validated_data)
    
        for genre in genre_data:
            genre, _ = Genre.objects.get_or_create(**genre)
            movie.genres.add(genre) 
    
        return movie
    
    def update(self, instance: Movie, validated_data: dict):
        genres_data = validated_data.pop('genres')
        instance.genres.set([])
        
        for genre in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre)
            instance.genres.add(genre)
            
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        
        return instance