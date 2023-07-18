from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blogHome(request):
    return HttpResponse("Welcome back to our BlogHome")

def blogPost(request,slug):
    return HttpResponse(f"Welcome back to our blogPost: {slug}")
