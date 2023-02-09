from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post,Comment
# Create your views here.

def home(request):
    return render(request,'blog/home.html')




def add_post(request : HttpRequest):
    if request.method == "POST":
        new_post = Post(Title= request.POST["Title"], Content = request.POST["Content"], is_published = request.POST["is_published"])
        new_post.save()
        return redirect("blog:latest blogs")
    
    return render(request, "blog/add_new_post.html")
    


def latest_blog(request : HttpRequest):
    latest_blog = Post.objects.all()
    context = {"latest_blog" : latest_blog}
    return render(request, "blog/blogs.html", context)





def update_blog(request : HttpRequest,blog_id):
 blog = Post.objects.get(id=blog_id)
 if request.method == "POST":
        blog.Title = request.POST["Title"]
        blog.Content = request.POST["Content"]
        blog.is_published = request.POST["is_published"]
        
        blog.save()
        return redirect("blog:latest blogs")

 return render(request, "blog/update_blog.html", {"blog" :blog})   



def delete_blog(request : HttpRequest, blog_id):
    blog = Post.objects.get(id=blog_id)
    blog.delete()
    return redirect("blog:latest blogs")

def search(request : HttpRequest):
  if request.method=="POST":
        user_input= request.POST['user_input'] 
        post =Post.objects.filter(Title__contains=user_input)
        return render(request, "blog/search.html", {'post':post})


def detailes(request : HttpRequest,blog_id):
    blog=Post.objects.get(id=blog_id)
    comments= Comment.objects.filter(blog=blog)
    return render(request, "blog/detail.html", {"blog" : blog ,"comments":comments})



def add_comment(request :HttpRequest,blog_id):
    if request.method=="POST":
        blog = Post.objects.get(id=blog_id) 
        new_comment=Comment(blog=blog,name=request.POST["name"], content = request.POST["content"])   
        new_comment.save()
    return redirect("blog:blog details", blog_id=blog_id)

 

 
  