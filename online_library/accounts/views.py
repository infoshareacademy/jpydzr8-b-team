from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MyRegisterForm, ProfileForm
from ol_project.logger_config import logger

def register(request):
    if request.method == "POST":
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f"New user registered: '{user.username}' (ID: {user.id})")
            return redirect("accounts:login")
        else:
            logger.warning("Invalid registration attempt.")
    else:
        form = MyRegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            logger.info(f"User '{request.user.username}' updated their profile.")
            return redirect("online_library:main")
        else:
            logger.warning(f"User '{request.user.username}' submitted invalid profile data.")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "registration/profile.html", {"form": form})
