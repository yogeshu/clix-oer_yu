from django.http import HttpResponse
from django.shortcuts import render
from .models import index , indexindex

# Create your views here.
def homepage_view(request, *args, **kwargs):
    # return HttpResponse ("<h1> hello i am new developer </h1>")
    
    destu1 = index()
    destu1.course_value = "science"
    destu1.coruse_student = "8th"
    destu1.course_description =  "lorem more more more more "
    destu1.course_title = "Communicative English level 1"
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
    destu1.course_value = "English"
    destu1.coruse_student = "8th"
    destu1.course_description =  "lorem more more more more "
    destu1.course_title = "Communicative English 1" 
    destu1.course_math = True

     
    destu2 = index()
    destu2.course_value = "English"
    destu2.coruse_student = "9th"
    destu2.course_description =  "lorem more"
    destu2.course_title = "Communicative English 2"
    destu2.course_math = False
     
    destu3 = index()
    destu3.course_value = "math"
    destu3.coruse_student = "8th"
    destu3.course_description =  "lorem more"
    destu3.course_title = "scienes courses"
    destu3.course_math = True
    

    
    
     
    destus= [ destu1, destu2, destu3 ]


    slider1= indexindex()
    slider1.slide_name= "Jennifer Thomas"
    slider1.slide_position= "Teacher"
    slider1.slide_bio= "i am a new deveopeer work on clix" 
    slider1.slide_co= "www.google.com"

    slider2= indexindex()
    slider2.slide_name= "Jennifer Thomas"
    slider2.slide_position= "developer"
    slider2.slide_bio= "i am a new deveopeer work on clix" 
    slider2.slide_co= "www.google.com"

    slider3= indexindex()
    slider3.slide_name= "Jennifer Thomas"
    slider3.slide_position= "developer"
    slider3.slide_bio= "i am a new deveopeer work on clix" 
    slider3.slide_co= "www.google.com"

    slider4= indexindex()
    slider4.slide_name= "Jennifer Thomas"
    slider4.slide_position= "developer"
    slider4.slide_bio= "i am a new deveopeer work on clix" 
    slider4.slide_co= "www.google.com"
    

    slider= [ slider1 , slider2 , slider3 , slider4  ]
    # return render(request , "domain.html", {})

    return render(request , "domain.html" , {'slider':slider, 'destus':destus})
def demo_view( request, *args, **kwargs):
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
    # return HttpResponse ("<h1> hello i am new demo_view </h1>")
    return render(request , "cscroll.html", {'destus':destus})
def cma_page(request , *args , **kwargs):
    return render(request, "cmspage.html" , {})

def vix_view( request,  *args, **kwargs):
    # return HttpResponse ("<h1> hello iam new to vix </h1>")
    return render(request , "vix.html", {})

def player_image_view( request, *args , **kwargs):
    return render(request, "player_image.html", {})

def module_cards_detail_view( request , *args , **kwargs):
    return render(request, "module_cards_detail.html", {})

def domain_sub_view( request , domain_name="maths"):
    return render(request, "module_cards_detail.html", {})

    return HttpResponse (domain_name)
