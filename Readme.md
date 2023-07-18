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