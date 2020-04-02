from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Movie, User, Rank
from django.db import IntegrityError
from django.urls import reverse_lazy


class RankListView(ListView):
    model = Rank
    template_name = 'rank/list.html'
    context_object_name = 'ranks'
    ordering = ['number']

    def get_queryset(self):
        return Rank.objects.filter(user=self.request.user).order_by('number')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(
            active=True).order_by('release_date')
        context['ranked_movies'] = Rank.objects.filter(
            user_id=self.request.user.id).values_list(
            'movie_id', flat=True)
        return context


class RankCreateView(LoginRequiredMixin, CreateView):
    model = Rank
    fields = ['number', 'review']

    def get_queryset(self):
        return Rank.objects.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        self.movie = get_object_or_404(Movie, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = Movie.objects.get(id=self.kwargs['pk'])
        context['ranked_movies'] = Rank.objects.filter(
            user_id=self.request.user.id).order_by('number')
        return context

    def form_valid(self, form):
        form.instance.movie = self.movie
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('number', 'Duplicate Rank or Movie')
            return self.form_invalid(form)


class RankUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Rank
    fields = ['number', 'review']

    def get_queryset(self):
        return Rank.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ranked_movies'] = Rank.objects.filter(
            user_id=self.request.user.id).order_by('number')
        return context

    def test_func(self):
        rank = self.get_object()
        if self.request.user == rank.user:
            return True
        return False


class RankDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Rank
    success_url = reverse_lazy('rank-list')

    def test_func(self):
        rank = self.get_object()
        if self.request.user == rank.user:
            return True
        return False
