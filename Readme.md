# Django Blog App

This is a Django Blog template integrated with tinyMCE Editor, using Bootstrap in a virtual environment.

## Functionality
1. **Blog Creation:** 
    - New blogs can be created and displayed using tinyMCE Editor. An admin account is required to write a post/blog.
2. **SignUp Functionality:** 
    - New users can sign up for the mCoder Blog.
3. **SignIn/SignOut Functionality:** 
    - Users may sign in and sign out as per their convenience.
4. **Comment Section to a Blog:** 
    - Only authenticated users have access to comment and reply.
5. **Reply Section:** 
    - Users may reply to a comment, limited to only one reply.
6. **Contact:** 
    - Users may contact the owner and share their feedback.

## Apps Used
- Bootstrap for Frontend
- Django for Backend
- tinyMCE Editor for writing blogs as admin

## How it Looks Like

### HomePage
![HomeWithoutLogin](https://github.com/ananty1/mCoder_blog/assets/105732693/d3f5bd2f-56ae-452d-aa31-5d5d7c227300)

### BlogPage
![Blog_page](https://github.com/ananty1/mCoder_blog/assets/105732693/e410c425-22ca-42c0-a015-84817bfd5e9e)

### Sample Blog Page
![blog_page_Sample](https://github.com/ananty1/mCoder_blog/assets/105732693/2d1f926f-7753-4bef-8148-2eaad7db9a93)

### Comment Section
![Comments](https://github.com/ananty1/mCoder_blog/assets/105732693/55ff205e-12ac-408e-8cce-1e8280657c29)

### Special Request
Do not forget to include `requirement.txt`.

## How Did We Achieve That?

Here's a step-by-step guide:

1. Start a project using `django-admin startproject project_name`.
2. Create an app for the project using `python3 manage.py startapp app_name`.
3. In the urls file of your project, include: `path('', include('blog.urls'))`.
4. In the urls of your app, include: 
    ```python
    urlpatterns = [
        path('', views.index , name='index'),
    ]
    ```
5. Update your views of your app:
    ```python
    def index(request):
        return HttpResponse("Welcome back to our Django")
    ```
6. Check using `python3 manage.py runserver`.

Remember, no app has `urls.py` initially, so you need to create one for each app.

## HTML TEMPLATE Inclusion

To include an HTML TEMPLATE:
1. Create a template and a static directory in the directory where your `manage.py` resides.
2. Add the templates directory to your settings:
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['templates'],         ## Here is the change
            'APP_DIRS': True,
            ........
        }
    ]
    ```
3. Create a `base.html` to act as the base for all related web-pages by extending it.

## Migrations

Tell Django that these are the updates by running migrations.

## Authentication and Authorization

Django has a built-in user authentication system. Use `django.contrib.auth` for authentication and authorization.

## Comments and Replies

Adding comments and replies is achieved by creating another model and form.

## Static Files

Don't forget to add the following to `settings.py` of your project:
```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
