from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from rest_framework.views import APIView, Request, Response, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication

from accounts.permissions import AccountMoviePermission

from .models import Movie
from .serializers import MovieSerializer

class MovieView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AccountMoviePermission]
    
class MovieCRUDView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AccountMoviePermission]
    lookup_field = 'id'