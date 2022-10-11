from django.urls import path

from rest_framework.authtoken import views
from . import views

urlpatterns = [
    path('users/register/', views.AccountRegisterView.as_view()),
    path('users/login/', views.AccountLoginView.as_view())
]