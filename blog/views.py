from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def blogHome(request):
    blogs = Post.objects.all().order_by('sno')[:50]
    context = {'blogs':blogs}

    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug = slug).first()
    context = {"post":post}
    return render(request,'blog/blogPost.html',context)


