from rest_framework import serializers

from .models import Review

class CriticSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'movie_id': {'read_only': True}, 'id': {'read_only': True},
            'movie': {'write_only': True, 'required': False}, 'stars': {'min_value': 1, 'max_value': 10}}
    
    critic = CriticSerializer(read_only=True)
    
    movie_id = serializers.SerializerMethodField()
    def get_movie_id(self, object):
        return object.movie.id
            
    def create(self, validated_data):
        critic = validated_data.pop('critic')
        movie = validated_data.pop('movie')

        review = Review.objects.create(
            **validated_data, movie=movie, critic=critic)
    
        return review