from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, RegisterForm, UserUpdateForm, UserCreationForm



# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if register_form.is_valid() and profile_form.is_valid():
            f = register_form.save(commit=False)
            p = profile_form.save(commit=False)
            first_name, last_name = register_form.cleaned_data.get('first_name'), register_form.cleaned_data.get('last_name') 

            f.username = f"{first_name} {last_name}"
            f.save()
            p.email = f.email
            p.save()

            messages.success(request, f"Your account has been created! You are now able to log in ")
            return redirect("login")
    else:

        register_form = RegisterForm()

    context = {
        "register_form": register_form,
        "profile_form": profile_form
        }

    return render(request, "users/register.html", context)


# add LOGIN_URL = "URL-NAME" in settings.py

