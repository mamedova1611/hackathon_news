
from django.urls import path
from .views import IndexView, NewsView, NewsDetailView, HistoryView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('history/<int:pk>/', HistoryView.as_view(), name='history'),
    path('news/<int:pk>/', NewsView.as_view(), name='news_list'),
    path('news/detail/<int:pk>', NewsDetailView.as_view(), name='news_detail')
]