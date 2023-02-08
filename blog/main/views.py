from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from .models import Post,Comment




# Create your views here.
def home_page(request):

    return render(request , 'main/home.html', {"Welcom" : "Welcome to our Blog Site"})


def add_new_blog(request : HttpRequest):
    if request.method == "POST":
        new_blog = Post(Title=request.POST["Title"],Content=request.POST["Content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])   
        new_blog.save()
        return redirect("main:home_page")
    return render(request , "main/add_blog.html")  


def show_only_what_is_ready_for_publish(request : HttpRequest):
    ready_blog = Post.objects.filter(is_published = True)
    context = {'ready_blog':ready_blog}
    return render(request , 'main/show_ready_blog.html' , context)       


def show_only_what_is_not_ready_for_publish(request : HttpRequest):
    not_ready_blog = Post.objects.filter(is_published = False)
    context = {'not_ready_blog':not_ready_blog}
    return render(request , 'main/show_not_ready_blog.html' , context)   


def show_all(request : HttpRequest):
    All_blog = Post.objects.all()
    

    context = {'all_blog' : All_blog }
    return render(request , 'main/show_all.html' , context)      

def post_Details(request : HttpRequest , post_id):
    show_post = Post.objects.get(id = post_id)
    review = Comment.objects.filter(post_rev = show_post)
    

    return render(request , 'main/post_details.html' , {'show_post' : show_post , "review":review})


def updateing_post(request : HttpRequest , post_id):
    update_post = Post.objects.get(id = post_id)
    update_post.publish_date = update_post.publish_date.isoformat
    if request.method == "POST":
        update_post.Title = request.POST["Title"]
        update_post.Content = request.POST["Content"]
        update_post.is_published = request.POST["is_published"]
        update_post.publish_date = request.POST["publish_date"]

        update_post.save()
        return redirect('main:show_all')
    return render(request , 'main/update_post.html',{'update_post':update_post})    
    



def Delete_post(request : HttpRequest , post_id):
    delete_post = Post.objects.get(id = post_id)
    delete_post.delete()
    return redirect ('main:show_all')



def search_post(request : HttpRequest  ): 
    if request.method == 'POST':
        Search_new = request.POST['Search_new']
        Search_title = Post.objects.filter(Title__contains = Search_new )
        return render(request , 'main/search_post.html' , {'Search_new':Search_new , 'Search_title':Search_title })
    else:    
        return render(request , 'main/search_post.html')   



def add_review(request : HttpRequest, post_id):

    if request.method == "POST":
        posts_one = Post.objects.get(id=post_id)
        new_review = Comment(post_rev = posts_one , name=request.POST["name"], content = request.POST["content"])
        new_review.save()

    return redirect("main:show_post", post_id=post_id)






