from django.shortcuts import render, redirect
from blogs.models import Blog, category as Category
from about.models import About
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth




def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='published').exclude(slug='').order_by('-created_at')[:5]
    posts = Blog.objects.filter(is_featured=False, status='published').exclude(slug='').order_by('-created_at')[:10]

    #fetch about us
    try:
        about = About.objects.get( )
    except:
        about = None


    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'category_id': None,
        'about': about,
        
    }

    return render(request, 'home.html', context)

def blogs (request, slug):
    return render(request,'blog.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')

    form = AuthenticationForm()    
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout (request):
    auth.logout(request)
    return redirect('login')






