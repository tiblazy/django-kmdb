from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .models import Review
from .serializers import ReviewSerializer
from .permissions import ReviewPermission
class ReviewMovieView(ListCreateAPIView):
    queryset = Review
    serializer_class = ReviewSerializer
    authentication_classes = [ReviewPermission]

class ReviewMovieByIdView(RetrieveDestroyAPIView):
    queryset = Review
    serializer_class = ReviewSerializer
    authentication_classes = [ReviewPermission]