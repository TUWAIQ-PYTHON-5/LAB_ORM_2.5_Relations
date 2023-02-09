from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post, Review
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


def post_Details(request : HttpRequest , post_id):

    show = Post.objects.get(id=post_id)

    return render(request ,'main/detail.html' ,{'show':show})






def Delete_post(request : HttpRequest , post_id):
    delete_post = Post.objects.get(id = post_id)
    delete_post.delete()
    return redirect ('main:index')


def update_post(request : HttpRequest , post_id):
    update_post = Post.objects.get(id = post_id)
    update_post.publish_date = update_post.publish_date.isoformat
    if request.method == "POST":
        update_post.title = request.POST["title"]
        update_post.content = request.POST["Content"]
        update_post.is_published = request.POST["is_published"]
        update_post.publish_date = request.POST["publish_date"]

        update_post.save()
    return render(request , 'main/update_post.html',{'update_post':update_post})


def search(request : HttpRequest  ): 
    if request.method == 'POST':
        search_post = request.POST("search post")
        search_title = Post.objects.filter(Title__contains = search_post )
        return render(request , 'main/search.html' , {'Search_title':search_title })
    return render(request, "main/search.html")


def add_review(request : HttpRequest, post_id):

    if request.method == "POST":
        comment = Post.objects.get(id=post_id)
        new_review = Review(rev =comment, name=request.POST["name"], content = request.POST["content"])
        new_review.save()

    return redirect("main:show_post", post_id = post_id)
