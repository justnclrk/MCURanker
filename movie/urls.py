from django.urls import path
from .views import MovieDetailView, MovieListView
from . import views

urlpatterns = [
    path('movie/<int:pk>', MovieDetailView.as_view(), name="movie-detail"),
    path('', MovieListView.as_view(), name="movie-list")
]
