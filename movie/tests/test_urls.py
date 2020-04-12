from django.test import SimpleTestCase
from django.urls import reverse, resolve
from movie.views import MovieListView, MovieDetailView


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('movie-list')
        self.assertEqual(resolve(url).func.view_class, MovieListView)

    def test_detail_url_resolves(self):
        url = reverse('movie-detail', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, MovieDetailView)
