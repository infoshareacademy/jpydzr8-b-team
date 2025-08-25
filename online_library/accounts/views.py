from django.shortcuts import render, redirect
from .forms import MyRegisterForm

def register(request):
    if request.method == "POST":
        form =MyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("online_library:main")
    else:
        form = MyRegisterForm()
    return render(request, "registration/register.html", {"form": form})
