from django.db import models

# Create your models here.


class Posts(models.Model):

    title = models.CharField(max_length=1024)
    content =  models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateField()


class Comment(models.Model):

    post_name = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=102)
    content =  models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
