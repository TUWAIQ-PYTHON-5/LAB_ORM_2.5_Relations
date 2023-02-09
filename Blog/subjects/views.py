from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpRequest
from .models import Review, Subject


def home_page(request : HttpRequest):
    return render(request,"subjects/home_page.html")


def write_page(request : HttpRequest):

    if request.method == "POST":
        new_subject = Subject(title= request.POST["title"], content = request.POST["content"], is_published = request.POST["is_published"], published_date=request.POST["published_date"])
        new_subject.save()
        return redirect("subjects:read_page")

    return render(request,"subjects/write.html")
    

def read_page(request :HttpRequest):
    
    subjects_save = Subject.objects.all()
    context = {"subjects_save" : subjects_save}
    return render(request,"subjects/read.html", context)
    


def details_page(request : HttpRequest,subject_id):
    subject = Subject.objects.get(id=subject_id)
    reviews = Review.objects.filter(subject=subject)

    return render(request,"subjects/subject_details.html", {"subject" : subject, "review": reviews})



def update_page(request : HttpRequest,subject_id):

    subject = Subject.objects.get(id=subject_id)
    
    if request.method == "POST":

        subject.title = request.POST["title"]
        subject.content = request.POST["content"]
        subject.is_published = request.POST["is_published"]
        
        subject.save()
        return redirect("subjects:read_page")

    return render(request,"subjects/update_subject.html", {"subject" : subject})

def delete_page(request : HttpRequest, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    return redirect("subjects:read_page")
    
def search_page(request : HttpRequest):
    
    if request.method == 'GET':
        search = request.GET.get("search")
        result_search = Subject.objects.filter(title__icontains=search)  

        return render(request,"subjects/result_search.html", {"result_search" : result_search})


def review(request : HttpRequest, subject_id):

    if request.method == "POST":
        subject = Subject.objects.get(id=subject_id)
        new_review = Review(subject=subject, name=request.POST["name"], content = request.POST["content"])
        new_review.save()

    return redirect("subjects:details_page", subject_id=subject_id)

    

def about_page(request : HttpRequest):
    return render(request,"subjects/about.html")


