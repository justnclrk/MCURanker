from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, F, Func
from django.views.generic import DetailView, ListView
from .models import Movie
from rank.models import Rank


class Round(Func):
    function = 'ROUND'
    arity = 2


class MovieListView(ListView):
    model = Movie
    template_name = 'movie/list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.filter(active=True).annotate(average_rank=Round(Avg('rank__number'), 1)).order_by(F('average_rank').asc(nulls_last=True))


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
