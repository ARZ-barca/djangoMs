from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'alireza z',
        'title': 'first post',
        'content': 'first post content',
        'date': 'mehr 1400'
    },
    {
        'author': 'amir z',
        'title': 'second post',
        'content': 'second post content',
        'date': 'azar 1400'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': about})

