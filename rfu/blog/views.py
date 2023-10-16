from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import BlogPost

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

class LikeView(View):
    def post(self, request, post_id):
        post = BlogPost.objects.get(id=post_id)
        post.like()
        return JsonResponse({'likes': post.likes}, status=200)
