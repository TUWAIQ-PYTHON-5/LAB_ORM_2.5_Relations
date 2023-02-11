from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.


def index(request : HttpRequest):
    
    
    posts = Post.objects.all()
    context = {"posts" : posts}

    return render(request, "main/index.html", context)



def add_post(request : HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content= request.POST["content"], is_published= request.POST["is_published"])
        new_post.save()

        return redirect("main:index_page")

    return render(request, "main/add_post.html")



def update(request : HttpRequest , post_id):
    post=Post.objects.get(id=post_id)
    post.publish_date = post.publish_date.isoformat

    if request.method == "POST":
        post.title=request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = request.POST["is_published"]
        post.publish_date = request.POST["publish_date"]

        post.save()
        return redirect("")

    return render(request , "" , {})
    