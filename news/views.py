from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostForm


def news(request):
    posts = Post.objects.all()
    return render(request, 'news.html', context={'posts': posts})


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news1.html'
    context_object_name = 'post1'


def new1(request):
    news1 = Post.objects.get(primary_key=1)
    return render(request, 'news1', context={'news1': news1})


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')
