<!-- Do not foget to pip install -r requirement.txt -->

# Django Blog App
This is a Django Blog template, integrated with tinyMCE Editor,using Bootstrap.
# Functionality--
    1)Blog Creation
    Any New blog can be created and shown in the Blog using tinyMCE Editor, admin is needed to write a post/blog
    2) SignUp functionality
    ----New user can sign Up to the mCoder Blog.
    2) SignIn/SignOut Functionality
    ---user may sign-in and sign Out as per their convenience.
    3) Comment Section to a Blog
    ---only the authenticated user have access to comment and reply.
    4) Reply Section
    ---user may reply to a comment,limit to only one reply.
    5) Contact 
    ---User may contact to owner and share their feedback.
# Apps used--
---- Bootstrap for front End
---- Django for backend
---- tinyMCE Editor for writing blogs as admin 






## How did we achieve that?
Step 1- Start a project using django-admin startproject project_name
Step 2- Create app for the project using python3 manage.py startapp app_name

Step 3 - In the urls file of your project ,write the following ----
    -----path('', include('blog.urls')),

Step 4 - IN the urls of your app include this--------
urlpatterns = [
    path('', views.index , name='index'),
]

Step 5- Update your views of your app ,

def index(request):
    return HttpResponse("Welcome back to our Django")

Step6- Check using python3 manage.py runserver


No app has urls.py initially,we need to create that for our every app.


So here we will create the blogs as they should ideally be , so we gonna use git too.

## Special request - Do not forget to write requirement.txt

###  Also we gonna install virtual enviornment virtualenv
----------- So this create a folder which includes an independent python--------------

This is to see any string ----path('<str:slug>',views.blogPost, name = 'blogPost'),

## Now next step is to include a HTML TEMPLATE which is achieved by.
i) Create a template and a staic directory in the directory where your manage.py resides
### Do not forget to add templates in your setting like-------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],         ## Here is the change
        'APP_DIRS': True,
        ........
    }
]


We wiil create a base.html which will act as base for all the related web-pages
How do we achieve that?
simply extend ,that's it

## NOw migrations---------->
tell django that these are the updates

# Create admin-user

# then create -super user

### Seems like search functionality will be the toughest part
------query = request.GET['query']
    blogs = Post.objects.filter(title__icontains=query)
    Yeah ,thankfully icontains pops up as our saviour \

## But next is authentication ,let's see
------Djnago has built in users authentication system
------authorization -permission
-------authentication---Your Identity

<!-- Django authentication is general ,can be used for any type of website,whenther blog ,or online search sites-->
So a good things is there is built-in modal for creating users, so signUp is easy.

To validate or authentication validation of a user ,django does have inbuilt- functions
--from django.contrib.auth import authenticate,login,logout
and if anyone is having time reading this-do not forget 
## Jaadu------
if user.is_authenticated in django let's u logged in.

## How to think about making Comments? Intersting question,huh!!
Adding comment is really intersting,which is nothing just another model and another form 

## To use static files do not forget to add this to settings.py of your project
-----STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]

## Well-well after successfully making a comment ,next turn is to do reply ,but i am not able to make proper blue-print to reply.

## Questions? I couldn't resolve,how the hell the looping reply inside the comments are going to be written .
As a first step, he saved the dictory[reply.sno]=[reply]
Note: One can only reply to the original comment

## Now Is the final one Editing the blog 
 We have used tinyMCE Editor for it.
 So In order to use tinyMCE ,one has to integrate this with Django,
 A tinyInject.js file has been create which is needed to change the content of the post as per html ,
 Let' integrate it---(using app's admin--(blog.admin))
 <<<<<<<<<<<<<=======================================>>>>>>>>>>>>>
    @admin.register(Post)
    class PostAdmin(admin.ModelAdmin):
    class Media:
        js  = ('tinyInject.js',)
<<<<<<<<<<<<<<<<<<<<<========================>>>>>>>>>>>>>>>>>>>>>
 And it's successfully done! 
 

 ## Before Ending this Blog Project ,
 One more thing to do ---- Blog view count
 
 And That's it 
 ## Happy Ending
 ## Journey to code begins forever..............
 
