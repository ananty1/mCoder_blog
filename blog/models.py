from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)


    def __str__(self):
        return f"{self.sno}){self.title}"
    

