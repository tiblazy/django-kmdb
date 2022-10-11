from pkgutil import get_data
from rest_framework import serializers

from .models import Movie

from genres.models import Genre
from genres.serializers import GenreSerializer

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    
    class Meta:
        model = Movie
        # fields = ['id', 'title', 'premiere', 'duration', 'classification', 'synopsis', 'genres']
        exclude = ['reviews']
        
    def create(self, validated_data):
        genre_data = validated_data.pop('genres')
        
        movie = Movie.objects.create(**validated_data)
    
        for genre in genre_data:
            genre, _ = Genre.objects.get_or_create(**genre)
            movie.genres.add(genre) 
    
        return movie
    
    def update(self, instance: Movie, validated_data: dict):
        pass