<!-- Do not foget to pip install -r requirement.txt -->

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


