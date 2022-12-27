from django.shortcuts import HttpResponse, render
from blog.models import Blog

data = {
    "blogs":[
        {
            "id":1,
            "title":"Komple Web Kursu",
            "image":"web_photo.jpg",
            "is_active":True,
            "is_home":False,
            "description":"Web alanında iyi bir kurs"
        },
         {
            "id":2,
            "title":"Python Kursu",
            "image":"code.png",
            "is_active":False,
            "is_home":False,
            "description":"Python alanında iyi bir kurs"
        },
         {
            "id":3,
            "title":"Django Kursu",
            "image":"django.png",
            "is_active":True,
            "is_home":True,
            "description":"Django alanında iyi bir kurs"
        },
    ]
}

# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True)
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request,"blog/blogs.html", context)

def blog_details(request, slug):
    blogs = data["blogs"]
    
    for blog in blogs:
        blog = Blog.objects.get(slug=slug)

    return render(request,"blog/blog-details.html", {
        "blog":blog
    })


