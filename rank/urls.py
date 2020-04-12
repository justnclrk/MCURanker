from django.urls import path
from .views import RankListView, RankCreateView, RankUpdateView, RankDeleteView, RankClearAll
from . import views

urlpatterns = [
    path('list', RankListView.as_view(), name="rank-list"),
    path('new/<str:slug>', RankCreateView.as_view(), name="rank-create"),
    path('update/<str:slug>', RankUpdateView.as_view(), name="rank-update"),
    path('delete/<str:slug>', RankDeleteView.as_view(), name="rank-delete"),
    path('clearall/<username>', RankClearAll, name='rank-clear-all'),
]
