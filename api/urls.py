from django.urls import path
from .views import PublicArticleListView, ArticleListView, ArticleDetailView, UserCreateView

urlpatterns = [
    path('articles/public/', PublicArticleListView.as_view(), name='public-articles'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('users/', UserCreateView.as_view(), name='user-create'),
]
