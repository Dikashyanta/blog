from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Blog, category as Category

from django.db.models import Q


# Create your views here.
def post_list_by_category(request, category_id):

    # fetch posts based on category_id and pass to template
    posts = Blog.objects.filter(category__id=category_id, status='published').exclude(slug='').order_by('-created_at')
    
    try:
        category_obj = Category.objects.get(id=category_id)
    except :
        
        return redirect('home')

    # category = get_object_or_404(Category, id=category_id)



    context = {
        'posts': posts,
        'category': category_obj,

    }

    return render(request, 'post_by_category.html', context)
def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='published') 
    context = {

        'single_blog': single_blog,
    }
    return render(request,'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')


    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published').exclude(slug='').order_by('-created_at')

    context = {
        'blogs': blogs,
        'keyword': keyword,
        }
    
    return render(request, 'search.html', context)


