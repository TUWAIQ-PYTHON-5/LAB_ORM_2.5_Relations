from django.db import models

class Subject(models.Model):

    title = models.CharField(max_length=256)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    content = models.TextField()
    
