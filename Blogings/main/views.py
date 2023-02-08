from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog, Comment
from datetime import date



def leatestBlogs(request : HttpRequest):
    leatestBlogs = Blog.objects.all()
    context = {"leatestBlogs" : leatestBlogs}
    return render(request, "main/leatestBlogs.html", context)
##################################################################
def addBlog(request : HttpRequest):
    if request.method == "POST":
        newBlog = Blog(title= request.POST["title"], content = request.POST["content"], isPublish = request.POST["isPublish"])
        newBlog.save()
        return redirect("main:leatestBlogs")
    return render(request, "main/addBlog.html")
##################################################################
def updateBlog(request : HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.writingDate = blog.writingDate.isoformat #to make it compatible with input value in html
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.isPublish = request.POST["isPublish"]
        blog.writingDate= request.POST["writingDate"]
        blog.save()
        return redirect("main:leatestBlogs")
    return render(request, "main/updateBlog.html", {"blog" : blog})
##################################################################
def blogDetail(request : HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    return render(request, "main/blogDetail.html", {"blog" : blog, "comments" : comments})
##################################################################
def deleteBlog(request : HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect("main:leatestBlogs")
##################################################################
def findBlog(request : HttpRequest):
    if request.method == "POST":
        toFind = request.POST['toFind']  
        result = Blog.objects.filter(title__contains=request.POST['toFind'] )
        return render(request, "main/findBlog.html", {'toFind' : toFind , 'result' : result})
    else:
        return render(request, "main/findBlog.html", {'toFind' : toFind})
##################################################################
def comment(request : HttpRequest, blog_id):

    if request.method == "POST":
        blog = Blog.objects.get(id=blog_id)
        newComment = Comment(blog = blog, name= request.POST["name"], content = request.POST["content"], rating= request.POST["rating"])
        newComment.save()

    return redirect("main:blogDetail", blog_id=blog_id)
