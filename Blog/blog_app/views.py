from django.shortcuts import render , redirect
from django.http import HttpRequest ,HttpResponse
from .models import Posts , Comment

# Create your views here.




def index(request : HttpRequest):

    blogs = Posts.objects.all()
    context = {
        "blog" : blogs
    }
    return render(request ,"blogs/index.html" , context)




def add_post(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        new_post = Posts(
            
            title = request.POST["title"],
            content = request.POST["content"],
            is_published = request.POST['is_published'],
            publish_date = request.POST["publish_date"]
        ).save()
        return redirect("blog:blogs_page")
    return render(request, "blogs/Add_post.html")




def detail_post(request : HttpRequest , post_id ):
    
    details = Posts.objects.get(id = post_id)
    result = Comment.objects.filter(post_name=details)

    return render(request , "blogs/post_details.html" , {"details" : details, "result" : result})


def post_update(request : HttpRequest , post_id ):

    post = Posts.objects.get(id = post_id)

    if request.method == "POST":
       
            
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST["is_published"]
            post.publish_date = request.POST["publish_date"]

            post.save()
            return redirect("blog:blogs_page")
    return render(request , "blogs/post_update.html" ,  {"post" : post})


def delete_post(request : HttpRequest, post_id):
    post = Posts.objects.get(id=post_id)
    post.delete()
    return redirect("blog:blogs_page")



def search(request : HttpRequest):

    if request.method == "GET": 

            post_name =  request.GET.get('search')      
            search_post = Posts.objects.filter(title__contains = post_name)
               
            return render(request , "blogs/search.html" , {"search_post" : search_post})





def add_comment(request : HttpRequest, post_id):

    if request.method == "POST":
        post = Posts.objects.get(id=post_id)
        new_comment = Comment(post_name=post, name=request.POST["name"], content = request.POST["content"])
        new_comment.save()

    return redirect("blog:details_post", post_id=post_id)




