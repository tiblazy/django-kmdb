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
        genres_data = validated_data.pop('genres')
        instance.genres.set([])
        
        for genre in genres_data:
            genres = Genre.objects.filter(name=genre["name"]).first()

            if not genres:
                new_genre = Genre.objects.create(**genre)
                instance.genres.add(new_genre)

            instance.genres.add(genres)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        
        return instance