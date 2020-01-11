from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Category


def home(request):
    return HttpResponse('Olá mundo!!')


def home_param(request, post_id):
    return HttpResponse(f'Olá mundo {post_id}')


def post_list(request):
    #name = 'Fernando'
    if 'category_id' in request.GET:
        # category = Category.objects.get(id=request.GET['category_id'])
        posts = Post.objects.filter(categories=request.GET['category_id'])
    else:
        posts = Post.objects.all()

    categories = Category.objects.all()
    return render(request, 'post_list.html', {
        'posts': posts,
        'categories': categories
    })


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()
    return render(request, 'post_show.html', {
        'post': post,
        'categories':categories
    })