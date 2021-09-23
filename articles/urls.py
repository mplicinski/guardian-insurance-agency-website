from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    path('create/', login_required(ArticleCreateView.as_view()), name='create'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', login_required(ArticleUpdateView.as_view()), name='update'),
    path('<slug:slug>/delete/', login_required(ArticleDeleteView.as_view()), name='delete'),
]
