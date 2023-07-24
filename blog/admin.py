from django.contrib import admin
from .models import Post,blogComment

# Register your models here.
admin.site.register((Post,blogComment))
