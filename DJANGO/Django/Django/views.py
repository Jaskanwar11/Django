from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hey there, How are you\nThis is the Home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("About")
    return render(request, 'website/about.html')


def contact(request):
    return HttpResponse("Contact")
    return render(request, 'website/index.html')