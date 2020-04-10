from django.urls import path
from .views import MovieDetailView, MovieListView
from . import views

urlpatterns = [
    path('', MovieListView.as_view(), name="movie-list"),
    path('movie/<str:slug>', MovieDetailView.as_view(), name="movie-detail")
]
