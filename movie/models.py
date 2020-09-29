from django.db import models
from PIL import Image


class Movie(models.Model):
    image = models.ImageField(
        default='default-movie.png', upload_to='movie_posters')
    title = models.CharField(max_length=60, unique=True)
    overview = models.TextField()
    phase = models.IntegerField()
    release_date = models.DateField()
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['release_date', 'phase']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
