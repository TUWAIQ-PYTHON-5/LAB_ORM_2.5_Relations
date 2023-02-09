from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=1024)
    Content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)#اسم الي بيكتب الكوممنت
    content = models.TextField()#محتوى الكومنت
    rating =  models.FloatField()#التقييم

    created_at = models.DateTimeField(auto_now_add=True)