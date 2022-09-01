
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import Http404
from .models import Category, Page, Post
from .forms import PostForm





# Create your views here.

def index(request):
    # categories = category.objects.filter(name='essay').order_by('date_added')
    categories = Category.objects.order_by('order')
    if request.user.is_authenticated:
        posts = Post.objects.order_by('date_added').reverse()
    else:
        posts = Post.objects.filter(status=1).order_by('date_added').reverse()
    context ={'blogName': settings.BLOGNAME,'welcomeWord': settings.WELCOME_WORD,'categories':categories,'posts':posts}
    return render(request, 'Papers/index.html',context)

def viewCategory(request,category_id):
    category  = Category.objects.get(id=category_id)
    categories = Category.objects.order_by('order')
    if request.user.is_authenticated:
        posts = Post.objects.filter(category=category).order_by('date_added').reverse()
    else:
        posts = Post.objects.filter(category=category,status=1).order_by('date_added').reverse()
    context ={'blogName': settings.BLOGNAME,'category':category,'categories':categories,'posts':posts}
    return render(request, 'Papers/viewCategory.html',context)

def viewPost(request,post_id):
    post  = Post.objects.get(id=post_id)
    """if not logged in and the post is not published, raise 404
    """
    if post.status == 1 or request.user.is_authenticated:
        categories = Category.objects.order_by('order')
        context ={'blogName': settings.BLOGNAME,'categories':categories,'post':post}
        return render(request, 'Papers/viewPost.html',context)
    else:
        raise Http404


def viewPage(request,page_id):
    page  = Page.objects.get(id=page_id)
    """if not logged in and the page is not published, raise 404
    """
    if page.status == 1 or request.user.is_authenticated:
        categories = Category.objects.order_by('order')
        context ={'blogName': settings.BLOGNAME,'categories':categories,'page':page}
        return render(request, 'Papers/viewPost.html',context)
    else:
        raise Http404


def newPost(request):
    if request.user.is_authenticated:
        categories = Category.objects.order_by('order')
        """add new post"""
        if request.method != 'POST':
            form = PostForm()
        else:
            form = PostForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('Papers:index')
        context = {'blogName': settings.BLOGNAME,'categories':categories,'form':form}
        return render(request,'Papers/newPost.html', context)
    else:
        raise Http404

    

