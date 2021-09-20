from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import Article
from .forms import ArticleForm

class ArticleListView(ListView):
    template_name = 'articles/list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/detail.html'

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Article, slug = slug_)


# @login_required
class ArticleCreateView(CreateView):
    template_name = 'articles/create-update.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/create-update.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Article, slug=slug_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/delete.html'

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Article, slug=slug_)

    def get_success_url(self):
        return reverse('articles:blog')



