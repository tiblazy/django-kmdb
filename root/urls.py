from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('accounts.urls')),
    path('api/movies/', include('movies.urls')),
    path('api/movies/', include('reviews.urls')),
]
