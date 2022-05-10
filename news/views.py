from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


def news(request):
    posts = Post.objects.all()
    return render(request, 'news.html', context={'posts': posts})


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'news1.html'
    context_object_name = 'post1'


def new1(request):
    news1 = Post.objects.get(primary_key=1)
    return render(request, 'news1', context={'news1': news1})
