from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=1024)
    content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateField()

class Comment(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()

