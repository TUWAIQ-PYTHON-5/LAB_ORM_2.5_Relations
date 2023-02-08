from django.db import models


class Blog(models.Model):
     Title=models.CharField(max_length=50)
     Content=models.TextField()
     is_published=models.BooleanField()
     publish_date=models.DateTimeField(auto_now_add=True)


class Rivew(models.Model):
     blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
     name=models.CharField(max_length=50)
     content=models.TextField()


