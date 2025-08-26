from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MyRegisterForm, ProfileForm

def register(request):
    if request.method == "POST":
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("online_library:main")
    else:
        form = MyRegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("online_library:main")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "registration/profile.html", {"form": form})
