from logging.handlers import RotatingFileHandler
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


packages = {
    "1": "Educational Software for Universities & Schools",
    "2": "Informational or Small Business Website",
    "3": "Ecommerce Website",
    "4": "Mobile Application",
    "5":"Enterprise Application",
    "6": "other"
}

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            obj = contact_form.save(commit=False)
            # obj.package = packages[f"{package_id}"]
            obj.save()
            messages.success(request, f"Message Sent Successfully! We will contact you shortly.")
            return redirect("home")
            
    else:
        contact_form = ContactForm()

    context = {
        "contact_form": contact_form
    }

    return render(request, "contact.html", context)

def add_blog(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        blog_form = BlogForm(request.POST)

        if blog_form.is_valid():
            obj = blog_form.save(commit=False)
            obj.author = user
            # obj.package = packages[f"{package_id}"]
            obj.save()
            messages.success(request, f"Blog Posted Successfully")
            return redirect("home")
            
    else:
        blog_form = BlogForm()

    context = {
        "blog_form": blog_form
    }

    return render(request, "add_blog.html", context)


def blog(request):
    blogs = Blog.objects.all().order_by("-date_created")

    context = {
        "blogs":blogs
    }

    return render(request, "blogs.html", context)

def view_blog(request, id):
    blog = Blog.objects.get(id=id)

    context = {
        "blog":blog
    }

    return render(request, "view_blog.html", context)