from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    return HttpResponse("home page")

def blogs(request):
    return HttpResponse("blogs")

def blog_details(request, id):
    return HttpResponse("blog details" + str(id))


