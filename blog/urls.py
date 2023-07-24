from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome , name='blogHome'),
    path('blogCommentfunc',views.blogCommentfunc, name = 'blogCommentfunc'),
    
    path('<str:slug>',views.blogPost, name = 'blogPost'),
]
