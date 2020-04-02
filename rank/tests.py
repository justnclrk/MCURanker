from django.contrib.auth.models import AnonymousUser, User
from django.test import Client, RequestFactory, SimpleTestCase, TestCase
from django.urls import reverse, resolve
from rank.models import Rank
from movie.models import Movie
from rank.views import RankListView, RankCreateView, RankUpdateView, RankDeleteView

# URLS


class TestUrls(SimpleTestCase):

    def test_rank_list_url_resolves(self):
        url = reverse('rank-list')
        self.assertEquals(resolve(url).func.view_class, RankListView)

    def test_rank_create_url_resolves(self):
        url = reverse('rank-create', args=[30])
        self.assertEquals(resolve(url).func.view_class, RankCreateView)

    def test_rank_update_url_resolves(self):
        url = reverse('rank-update', args=[30])
        self.assertEquals(resolve(url).func.view_class, RankUpdateView)

    def test_rank_delete_url_resolves(self):
        url = reverse('rank-delete', args=[30])
        self.assertEquals(resolve(url).func.view_class, RankDeleteView)

# VIEWS


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tester', email='test@gmail.com', password='top_secret')

    def test_rank_list_view(self):
        request = RequestFactory().get('list')
        view = RankListView()
        view.setup(request)
