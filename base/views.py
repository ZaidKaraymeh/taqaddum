from django.shortcuts import redirect, render
from django.contrib import messages

from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request, "home.html")

def services(request):
    return render(request, "services.html")


packages = {
    "1": "Educational Software for Universities & Schools",
    "2": "Informational or Small Business Website",
    "3": "Ecommerce Website",
    "4": "Mobile Application"
}

def contact(request, package_id):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            obj = contact_form.save(commit=False)
            obj.package = packages[f"{package_id}"]
            print(obj)
            obj.save()
            messages.success(request, f"Message Sent Successfully! We will contact you shortly.")
            return redirect("home")
            
    else:
        contact_form = ContactForm()

    context = {
        "contact_form": contact_form
    }

    return render(request, "contact.html", context)