import imp
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# posts = [
#     {
#         'author': 'alireza z',
#         'title': 'first post',
#         'content': 'first post content',
#         'date_posted': 'mehr 1400'
#     },
#     {
#         'author': 'amir z',
#         'title': 'second post',
#         'content': 'second post content',
#         'date_posted': 'azar 1400'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': about})

