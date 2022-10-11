from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieView.as_view()),
    path('<int:id>/', views.MovieCRUDView.as_view()),
]