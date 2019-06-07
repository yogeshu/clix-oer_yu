from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
    # return HttpResponse ("<h1> hello i am new developer </h1>")
    return render(request , "Elibrary.html", {})


def about_view(request, *args, **kwargs):
    # return HttpResponse ("<h1> hello i am new about_view </h1>")
    return render(request , "about.html", {})


def domain_view(request,  *args, **kwargs):
    # return HttpResponse ("<h1> hello iam new to domain_vix </h1>")
    return render(request , "domain.html", {})


def demo_view( request, *args, **kwargs):
    # return HttpResponse ("<h1> hello i am new demo_view </h1>")
    return render(request , "vix.html", {})


def vix_view( request,  *args, **kwargs):
    # return HttpResponse ("<h1> hello iam new to vix </h1>")
    return render(request , "vix.html", {})

