from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.core.paginator import Paginator


def sampleapp_index(request):
    posts = Post.objects.all().order_by('-created_on')
    most_recent = Post.objects.order_by('-created_on')[:5]
    
    paginator = Paginator(posts, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "posts": posts,
        'most_recent': most_recent,
    }
    return render(request, "sampleapp_index.html", context)


def sampleapp_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')

    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "sampleapp_category.html", context)


def sampleapp_detail(request, slug):
    post = Post.objects.get(slug=slug)


    context = {
        "post": post,
    }
    return render(request, "sampleapp_detail.html", context)


def error_404(request, exception):
    return render(request, "404.html")
