from mcurank.utils import unique_slug_generator
from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie
from django.urls import reverse
from django.db.models.signals import pre_save

# Current Active Movie Count
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
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'movie'], name='user_unique_movie')
        ]
        ordering = ['number']

    def __str__(self):
        return self.user.username + "'s " + self.movie.title + " Rank"

    def get_absolute_url(self):
        return reverse('rank-list')

# unique_slug_generator from Django Code Review #2 | joincfe.com/youtube/


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post_receiver, sender=Rank)
