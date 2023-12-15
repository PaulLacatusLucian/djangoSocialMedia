from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Lacatus Paul',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'datePosted': '15.12.2023'
    },
    {
        'author': 'Maier Gia',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'datePosted': '16.12.2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
