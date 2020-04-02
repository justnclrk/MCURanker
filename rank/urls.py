from django.urls import path
from .views import RankListView, RankCreateView, RankUpdateView, RankDeleteView
from . import views

urlpatterns = [
    path('list', RankListView.as_view(), name="rank-list"),
    path('new/<int:pk>', RankCreateView.as_view(), name="rank-create"),
    path('update/<int:pk>', RankUpdateView.as_view(), name="rank-update"),
    path('delete/<int:pk>', RankDeleteView.as_view(), name="rank-delete"),
]
