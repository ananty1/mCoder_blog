from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Post,blogComment
from django.contrib.auth.models import User
from blog.templatetags import extras
# Create your views here.

def blogHome(request):
    blogs = Post.objects.all().order_by('sno')[:50]
    context = {'blogs':blogs}

    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    blog = Post.objects.filter(slug = slug).first()
    comments = blogComment.objects.filter(blog = blog,parent=None)
    replies = blogComment.objects.filter(blog=blog).exclude(parent=None)
    repDict={}

    for reply in replies:
        if reply.parent==None:
            pass
        else:
            if reply.parent.sno not in repDict.keys():
                repDict[reply.parent.sno]=[reply]
            else:
                repDict[reply.parent.sno].append(reply)
    
    context = {"post":blog,'comments':comments,'replyDict':repDict}
    return render(request,'blog/blogPost.html',context)

#APIS to comment
def blogCommentfunc(request):
    if(request.method=="POST"):
        Comment = request.POST.get('comment')
        user = request.user
        blogSno = request.POST.get('blogSno')
        parentSno = request.POST.get('parentSno')
        blog = Post.objects.get(sno=blogSno)
        if(parentSno==""):
            comment = blogComment(comment=Comment,user=user,blog=blog)
            comment.save()
            messages.success(request,"Your comment is succesfull")
        else:
            parent = blogComment.objects.get(sno=parentSno)
            comment = blogComment(comment=Comment,user=user,blog=blog,parent=parent)
            comment.save()
            messages.success(request,"You have posted a reply.")

        
        return redirect(f"/blog/{blog.slug}")
    return HttpResponse("Error 404 ,Request not being entertained")
    
    


