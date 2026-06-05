from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, category as Category

# Create your views here.
def post_list_by_category(request, category_id):

    # fetch posts based on category_id and pass to template
    posts = Blog.objects.filter(category__id=category_id, status='published').order_by('-created_at')
    category_obj = Category.objects.get(id=category_id)
    context = {
        'posts': posts,
        'category': category_obj,
    }
    return render(request, 'post_by_category.html', context)