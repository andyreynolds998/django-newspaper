from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
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

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDeleteView(
    LoginRequiredMixin, 
    UserPassesTestMixin, 
    DeleteView,
    ):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleUpdateView(
    LoginRequiredMixin, 
    UserPassesTestMixin, 
    UpdateView,
    ):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'