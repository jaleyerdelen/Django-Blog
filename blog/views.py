from django.shortcuts import HttpResponse, render

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
        "blogs":data["blogs"]
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs":data["blogs"]
    }
    return render(request,"blog/blogs.html", context)

def blog_details(request, id):
    blogs = data["blogs"]
    selectedBlog = None
 
    for blog in blogs:
        if blog["id"] == id:
            selectedBlog = blog

    #Comprehension
    # blogs = data["blogs"]
    # selectedBlog = [blog for blog in blogs if blog["id"] == id[0]]

    return render(request,"blog/blog-details.html", {
        "blog":selectedBlog
    })


