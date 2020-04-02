from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie
from django.urls import reverse

movies = Movie.objects.filter(active=True)
movie_count = movies.count()
movie_list = [tuple([movie, movie]) for movie in range(1, movie_count+1)]

movie_list_and_placeholder = [('', 'No Rank')] + movie_list


class Rank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE)
    number = models.IntegerField(
        choices=movie_list_and_placeholder, blank=True, null=True)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'movie'], name='user_unique_movie'),
            models.UniqueConstraint(
                fields=['user', 'number'], name='user_unique_rank')
        ]

    def __str__(self):
        return self.user.username + "'s " + self.movie.title + " Rank"

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.movie.pk})
