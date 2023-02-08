from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post , Review


# Create your views here.

def index(request : HttpRequest):
    
    return render(request, 'main/index.html')


def post_detail(request : HttpRequest):

    if request.method == "POST":
        new_blog = Post(title= request.POST["title"], content = request.POST["content"], is_published = request.POST["is_published"], publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("main:latest_blog_page")


    return render(request, "main/post_detail.html")



def latest_blog(request : HttpRequest):

    display = int(request.GET.get("display", 10))

    latest_blog = Post.objects.all()

    context = {"latest_blog" : latest_blog}
    return render(request, "main/index.html", context)



def update_blog(request : HttpRequest, blog_id):

    blog = Post.objects.get(id=blog_id)
    blog.publish_date = blog.publish_date.isoformat 
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.publish_date = request.POST["publish_date"]

        blog.save()
        return redirect("main:latest_blog_page")

    return render(request, "main/update.html", {"main" : blog})


def blog_detail(request : HttpRequest, blog_id):

    blog = Post.objects.get(id=blog_id)
    reviews = Review.objects.filter(Post=blog)
    context =  {
        "Post" : blog, 
        "reviews" : reviews
        }


    return render(request, "main/detail.html", context)
# 

def delete_blog(request : HttpRequest, blog_id):
    blog = Post.objects.get(id=blog_id)
    blog.delete()
    return redirect("main:latest_blog_page")




def search_blog(request : HttpRequest):
    if request.method == "POST":
        search = request.POST['search']
        search_blog = Post.objects.filter(title__contains=search)

        return render(request, "main/search.html", {'search_blog':search_blog }) 
    else:
        return render(request, "main/search.html", {})



def add_review(request : HttpRequest, blog_id):

    if request.method == "POST":
        blog = Post.objects.get(id=blog_id)
        new_review = Review(blog=blog, name=request.POST["name"], content = request.POST["content"], rating = request.POST["rating"])
        new_review.save()

    return redirect("main:blog_detail", blog_id=blog_id)