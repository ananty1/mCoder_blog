from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=50)
    content = models.TextField()
    views = models.IntegerField(default=0)
    img = models.CharField(max_length=500)
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)


    def __str__(self):
        return f"{self.sno}){self.title}"
    
class blogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.sno}){self.comment[:10]} by {self.user}"
    

