from django.urls import path

from .views import ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', ArticleUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', ArticleDeleteView.as_view(), name='delete'),
]
