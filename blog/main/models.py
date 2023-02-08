from django.db import models

# Create your models here.

class Post (models.Model):
   
    Title = models.CharField(max_length=1024)
    Content = models.TextField(blank=True)
    is_published = models.BooleanField(blank=True)
    publish_date =models.DateTimeField()


class Comment (models.Model):
    post_rev = models.ForeignKey(Post , on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)