from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Rank
from movie.models import Movie
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.db.models import F


class RankListView(ListView):
    model = Rank
    template_name = 'rank/list.html'
    context_object_name = 'ranks'

    def get_queryset(self):
        return Rank.objects.filter(user=self.request.user).order_by(F('number').asc(nulls_last=True))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(
            active=True).order_by('release_date')
        context['ranked_movies'] = Rank.objects.filter(
            user_id=self.request.user.id).values_list(
            'movie_id', flat=True)
        return context


class MovieIsActiveMixin:
    def dispatch(self, request, *args, **kwargs):
        self.movie = get_object_or_404(Movie, slug=kwargs['slug'])
        if self.movie.active == True:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class RankCreateView(LoginRequiredMixin, MovieIsActiveMixin, CreateView):
    model = Rank
    fields = ['number', 'review']

    def get_queryset(self):
        return Rank.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = Movie.objects.get(slug=self.kwargs['slug'])
        context['ranked_movies'] = Rank.objects.filter(
            user_id=self.request.user.id)
        return context

    def form_valid(self, form):
        form.instance.movie = self.movie
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error(
                'movie', 'You already ranked and reviewed this movie')
            return self.form_invalid(form)


class RankUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Rank
    fields = ['number', 'review']

    def get_queryset(self):
        return Rank.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ranked_movies'] = Rank.objects.filter(
            user_id=self.request.user.id)
        return context

    def test_func(self):
        rank = self.get_object()
        if self.request.user == rank.user:
            return True
        return False

    def form_valid(self, form):
        object = self.get_object()
        current_rank = Rank.objects.get(id=object.id)
        users_ranks = Rank.objects.filter(user_id=self.request.user)
        for rank in users_ranks:
            if rank.number:
                if rank.number == form.instance.number:
                    rank.number = current_rank.number
            rank.save()
        return super().form_valid(form)


class RankDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Rank
    success_url = reverse_lazy('rank-list')

    def test_func(self):
        rank = self.get_object()
        if self.request.user == rank.user:
            return True
        return False
