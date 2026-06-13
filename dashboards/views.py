from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import category as Category, Blog
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .forms import BlogPostForm, categoryForm
from django.contrib.auth.models import User


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        
        'category_count': category_count,
        'blogs_count':blogs_count,
       
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    categories_list = Category.objects.all()
    context = {
        'categories': categories_list,
    }
    return render(request, 'dashboard/categories.html', context)

def add_category(request):
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = categoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
    category_obj = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = categoryForm(request.POST, instance=category_obj)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = categoryForm(instance=category_obj)
    context ={
        'form': form,
        'category': category_obj,
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)
       
def add_post(request):
    if request.method == 'POST' :
        
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temporarily saving the form
            post.author = request.user
            post.save()
            return redirect('posts')
    
    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)


def edit_post(request,pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')


    form = BlogPostForm(instance=post)
    context ={
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')

def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'dashboard/users.html', context)





