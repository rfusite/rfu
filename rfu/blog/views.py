from django.shortcuts import render
from .models import BlogPost


def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})
