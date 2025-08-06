"Definiuje wzorce adresow URL dla online_libraries"

from django.urls import path
from . import views

app_name = 'online_libraries'
urlpatterns = [
    #strona glowna
    path('', views.main, name='main'),
    #strona do logowania
    path('sign_in/', views.signin, name='sign_in'),
    #storna rejestracji
    path('sign_up/', views.signup, name='sign_up'),
    # strona z baza ksiazek
    path('books_library/', views.books_library, name='books_library'),
    #strona about_us
    path('about_us/', views.about_us, name='about_us'),
]