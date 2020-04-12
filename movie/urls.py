from django.urls import path
from .views import MovieDetailView, MovieListView
from . import views

urlpatterns = [
    path('', MovieListView.as_view(), name="movie-list"),
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name="movie-detail")
]
