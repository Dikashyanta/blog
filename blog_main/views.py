

from django.shortcuts import render
from blogs.models import Blog, category


def home(request):
    categories = category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='published').order_by('-created_at')[:5]
    context = {
        'categories': categories,
        'featured_posts': featured_posts
    }

    return render(request, 'home.html', context)
