from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blogHome(request):
    return render(request,'blog/blogHome.html')

def blogPost(request,slug):
    # return HttpResponse(f"Welcome back to our blogPost: {slug}")
    return render(request,'blog/blogPost.html')
