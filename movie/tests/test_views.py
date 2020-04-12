from django.test import TestCase, Client
from django.urls import reverse
from movie.models import Movie
from django.contrib.auth.models import User
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='TestUser1',
            password='testingthesenuts',
            email='testuser@blackplanet.com'
        )

        self.movie_list_url = reverse('movie-list')
        self.movie_detail_url = reverse('movie-detail', args=['movie1'])
        self.movie1 = Movie.objects.create(
            title='movie1',
            release_date=2011,
            phase=2,
            overview='Pretty good movie'
        )

    def test_movie_list_GET(self):
        response = self.client.get(self.movie_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie/list.html')

    def test_movie_detail_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(self.movie_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie/movie-detail.html')
