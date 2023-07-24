from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    # Fetch posts
    posts = Post.objects.all().order_by('-views')[:3]
    context = {'posts':posts}
    return render(request,'home/home.html',context)

def about(request):
    messages.success(request,'Thank You for visiting Us')
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if(len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<4):
            messages.error(request,'Please fill the form Correctly')
        
        else:
            contact = Contact(name = name,email = email,phone = phone,content = content)
            contact.save()
            messages.success(request,'Your Form is submitted succesfully')

    return render(request,'home/contact.html')

def search(request):
    query = request.GET['query']
    
    if len(query)>80 or len(query)<1:
        blogs = Post.objects.none()
    else: 
        blogTitle= Post.objects.filter(title__icontains=query)
        blogContent = Post.objects.filter(content__icontains=query)
        blogs = blogTitle.union(blogContent)

            
    if blogs.count()==0  :
        messages.warning(request,'No Search Result Found! Please recheck your query')
    params = {"blogs":blogs,'query':query}
    return render(request,'home/search.html',params)

# Authentication API's

def handleSignUp(request):
    if request.method =="POST":
        #get the parameters
        username = request.POST["username"]
        try:
            User.objects.get(username=username)
            messages.error(request,'Username already exits')
            return redirect('home')

        except Exception as e:
            pass
        
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        #Check for Validity/Error in INput
        if len(username)>20 :
            messages.error(request,'Username must be below 20 characters')
            return redirect('home')
        if not username.isalnum() :
            messages.error(request,'Username must be contain only characters and string.')
            return redirect('home')
        
        if pass1!=pass2:
            messages.error(request,'Password do not match')
            return redirect('home')
            


        #Create the user
        myUser = User.objects.create_user(username,email,pass1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.save()
        messages.success(request,'You have succesfully signed Up')

        return redirect('home')
        
    else:
        return HttpResponse("Error 404! Not Found")
    
def handleLogIn(request):
    if request.method=='POST':
        username = request.POST['logInusername']
        password = request.POST['logInpassword']

        user = authenticate(username=username,password=password)

        if user!=None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
        
            return redirect("home")
        else:
            messages.error(request,"InValid Credentials,Please try again")
            return redirect("home")
        
    return HttpResponse("Error 404! Not Found")

def handleLogOut(request):
    logout(request)
    messages.success(request,"You have succesfully log out.")
    return redirect("home")


