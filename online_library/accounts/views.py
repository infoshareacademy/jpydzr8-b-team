from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Rejestracja uzytkownika"""
    if request.method != 'POST':
        #wyswietlanie pustego formularza rejestracji uzytkownika
        form = UserCreationForm()
    else:
        #przetworzenie wypelnionego formularza
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #zalogowanie uzytkownika, a nastepnie przekierowanie go na strone glowna
            login(request, new_user)
            return redirect('online_libraries:main')
        #wyswietlenie pustego formularza
    context = {'form': form}
    return render(request, 'registration/register.html', context)
