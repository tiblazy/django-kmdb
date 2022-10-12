from django.urls import path

from rest_framework.authtoken import views

from . import views

urlpatterns = [
    path('', views.AccountView.as_view()),
    path('register/', views.AccountRegisterView.as_view()),
    path('login/', views.AccountLoginView.as_view()),
    path('<int:user_id>/', views.AccountFilterView.as_view()),
]