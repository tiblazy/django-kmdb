from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.views import Request, Response,status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination

from movies.models import Movie

from .models import Review
from .serializers import ReviewSerializer
from .permissions import ReviewPostPermission, ReviewDeletePermission

class ReviewValidationError(ValidationError):
    status_code = 403
    default_detail = {'detail': 'Review already exists.'}

class ReviewMovieView(ListCreateAPIView, PageNumberPagination):
    queryset = Review
    serializer_class = ReviewSerializer
    permission_classes = [ReviewPostPermission]
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    lookup_url_kwarg = 'movie_id'
    
    def get(self, _: Request, movie_id: int) -> Response:
        reviews = Review.objects.filter(movie=get_object_or_404(Movie, pk=movie_id))
        result_page = self.paginate_queryset(reviews)
        serializer = ReviewSerializer(result_page, many=True)
        
        return self.get_paginated_response(serializer.data)
    
    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, pk=movie_id)
        prev_reviews = Review.objects.filter(movie=movie.id, critic=request.user.id)
        
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if len(prev_reviews)>0:
            raise ReviewValidationError()
        
        serializer.save(movie=movie, critic=request.user)
                
        return Response(serializer.data, status.HTTP_201_CREATED)
    
class ReviewMovieByIdView(RetrieveDestroyAPIView):
    queryset = Review
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewDeletePermission]
    lookup_field = 'id'
    lookup_url_kwarg = 'review_id'