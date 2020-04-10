from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Avg, F
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Movie
from rank.models import Rank


class MovieListView(ListView):
    model = Movie
    template_name = 'movie/list.html'
    context_object_name = 'movies'
    ordering = ['rank__number']

    def get_queryset(self):
        return Movie.objects.filter(active=True).annotate(Avg('rank__number')).distinct()


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_ranks'] = Rank.objects.filter(
            movie__slug=self.kwargs['slug']).order_by('-created_at')
        context['average_rank'] = Rank.objects.filter(
            movie__slug=self.kwargs['slug']).aggregate(Avg('number'))
        try:
            user_rank = Rank.objects.filter(
                movie__slug=self.kwargs['slug']).get(user_id=self.request.user)
        except Rank.DoesNotExist:
            user_rank = None
        context['ranked_movie'] = user_rank
        return context
