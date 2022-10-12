from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Movie
from .serializers import MovieSerializer
from .permissions import MoviePermission

class MovieView(ListCreateAPIView, PageNumberPagination):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [MoviePermission]
    pagination_class = PageNumberPagination
    
class MovieCRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [MoviePermission]
    lookup_field = 'id'
    lookup_url_kwarg = 'movie_id'