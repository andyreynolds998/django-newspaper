from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    fields = ['title', 'author', 'body', 'date']

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ['title', 'author', 'body']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('home')

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ['title', 'body']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'