from django.db import models

# Create your models here.


class Blog(models.Model):

    title       = models.CharField(max_length=200)
    content     = models.TextField()
    isPublish   = models.BooleanField()
    writingDate = models.DateTimeField(auto_now_add=True)
#############################################################
class Comment(models.Model):

    blog        = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name        = models.CharField(max_length=512)
    content     = models.TextField()
    rating      = models.FloatField()
    created_at  = models.DateTimeField(auto_now_add=True)