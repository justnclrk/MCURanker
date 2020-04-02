from django.contrib.auth.models import AnonymousUser, User
from django.test import Client, RequestFactory, SimpleTestCase, TestCase
from django.urls import reverse, resolve
from movie.models import Movie
from movie.views import MovieDetailView

# URLS


# class TestUrls(SimpleTestCase):

#     def test_movie_detail_url_resolves(self):
#         url = reverse('movie-detail', args=[30])
#         self.assertEquals(resolve(url).func.view_class, MovieDetailView)

# # VIEWS


# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.factory = RequestFactory()
#         self.movie = Movie.objects.create(
#             id=30, title='Squirrel Girl', phase=6)
#         self.user = User.objects.create_user(
#             username='tester', email='test@gmail.com', password='top_secret')

#     def test_movie_detail_view(self):
#         request = RequestFactory().get('movie-detail')
#         view = MovieDetailView()
#         view.setup(request)
