from django.shortcuts import render
from blogs.models import Blog, category as Category


def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='published').order_by('-created_at')[:5]
    posts = Blog.objects.filter(is_featured=False, status='published').order_by('-created_at')[:10]

    

    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'category_id': None,
        
    }

    return render(request, 'home.html', context)