from django.http import HttpResponse
from django.shortcuts import render
from .models import index

# Create your views here.
def homepage_view(request, *args, **kwargs):
    # return HttpResponse ("<h1> hello i am new developer </h1>")
    
    destu1 = index()
    destu1.course_value = "science"
    destu1.coruse_student = "8th"
    destu1.course_description =  "lorem more more more more "
    destu1.course_title = "Math courses"
    destu1.course_math = True
    destu1.course_science =True
    destu1.course_english= True

     
    destu2 = index()
    destu2.course_value = "science"
    destu2.coruse_student = "9th"
    destu2.course_description =  "lorem more"
    destu2.course_title = "sciene courses"
    destu2.course_math = False
     
    destu3 = index()
    destu3.course_value = "math"
    destu3.coruse_student = "8th"
    destu3.course_description =  "lorem more"
    destu3.course_title = "scienes courses"
    destu3.course_math = True
    
     
    destus= [ destu1, destu2, destu3 ]

    return render(request , "Elibrary.html", {'destus':destus})
 



def about_view(request, *args, **kwargs):
    # return HttpResponse ("<h1> hello i am new about_view </h1>")
    return render(request , "about.html", {})


def domain_view(request,  *args, **kwargs):
    # return HttpResponse ("<h1> hello iam new to domain_vix </h1>")
     
    destu1 = index()
    destu1.course_value = "math"
    destu1.coruse_student = "8th"
    destu1.course_description =  "lorem more more more more "
    destu1.course_title = "Math courses"
    destu1.course_math = True

     
    destu2 = index()
    destu2.course_value = "science"
    destu2.coruse_student = "9th"
    destu2.course_description =  "lorem more"
    destu2.course_title = "sciene courses"
    destu2.course_math = False
     
    destu3 = index()
    destu3.course_value = "math"
    destu3.coruse_student = "8th"
    destu3.course_description =  "lorem more"
    destu3.course_title = "scienes courses"
    destu3.course_math = True
    

    
    
     
    destus= [ destu1, destu2, destu3 ]
    # return render(request , "domain.html", {})

    return render(request , "domain.html" , {'destus':destus})
def demo_view( request, *args, **kwargs):
    # return HttpResponse ("<h1> hello i am new demo_view </h1>")
    return render(request , "cscroll.html", {})


def vix_view( request,  *args, **kwargs):
    # return HttpResponse ("<h1> hello iam new to vix </h1>")
    return render(request , "vix.html", {})

def player_image_view( request, *args , **kwargs):
    return render(request, "player_image.html", {})

