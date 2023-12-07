from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import BlogPost
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog(request):
    posts_list = BlogPost.objects.all().order_by('-date')
    paginator = Paginator(posts_list, 4)  # 5 постов на странице

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, показываем первую страницу.
        posts = paginator.page(1)
    except EmptyPage:
        # Если страница вне диапазона, показываем последнюю страницу результатов.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'posts': posts})


class LikeView(View):
    def post(self, request, post_id):
        post = BlogPost.objects.get(id=post_id)
        post.like()
        return JsonResponse({'likes': post.likes}, status=200)
