from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieView.as_view()),
    path('<int:movie_id>/', views.MovieCRUDView.as_view()),
]