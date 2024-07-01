from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .models import BlogPost
from django.core.paginator import Paginator
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    search_query = request.GET.get('search','')
    posts = BlogPost.objects.all().order_by('-publication_date')

    if search_query:
        posts = posts.filter(title__icontains=search_query) | posts.filter(content__icontains=search_query)

    paginator = Paginator(posts,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    context = {
        'posts': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj
    }

    return render(request,'home.html',context)

def blogDetails(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    print(post)
    return render(request,'blogDetails.html',{'post':post})

@login_required
def newBlog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('allBlogs')
    else:
        form = BlogPostForm()
    return render(request,'addBlog.html',{'form': form, 'form_title': 'New Post'})


@login_required
def blogEdit(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    if post.author != request.user:
        return redirect('allBlogs')
    if request.method == 'POST':
        form = BlogPostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('allBlogs')
    else:
        form = BlogPostForm(instance=post) 
    return render(request, 'blogUpdate.html', {'form': form, 'form_title': 'Edit Post'})


@login_required
def blogDelete(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('allBlogs')
    return render(request,'blogDelete.html',{'post':post})


# Register

def register(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('allBlogs')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})


# sign In 

def signIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('allBlogs')
    else:
        form = AuthenticationForm
    return render(request,'signIn.html',{'form':form})


# Logout

def logout_view(request):
    logout(request)
    return redirect('allBlogs')
