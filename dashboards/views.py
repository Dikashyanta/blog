from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import category as Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import categoryForm


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




