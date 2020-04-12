from django.urls import path
from .views import RankListView, RankCreateView, RankUpdateView, RankDeleteView, RankClearAll
from . import views

urlpatterns = [
    path('list', RankListView.as_view(), name="rank-list"),
    path('new/<slug:slug>', RankCreateView.as_view(), name="rank-create"),
    path('update/<slug:slug>', RankUpdateView.as_view(), name="rank-update"),
    path('delete/<slug:slug>', RankDeleteView.as_view(), name="rank-delete"),
    path('clearall/<username>', RankClearAll, name='rank-clear-all'),
]
