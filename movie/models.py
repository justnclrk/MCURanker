from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Movie(models.Model):
    image = models.ImageField(
        default='default-movie.png', upload_to='movie_posters')
    title = models.CharField(max_length=60)
    overview = models.TextField()
    phase = models.IntegerField()
    release_date = models.IntegerField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)
