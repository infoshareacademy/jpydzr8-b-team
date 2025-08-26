"Definiuje wzorce adresow URL dla online_library"

from django.urls import path
from . import views

app_name = 'online_library'
urlpatterns = [
    #strona glowna
    path('', views.main, name='main'),
    # strona z baza ksiazek
    path('books/', views.books_library, name='books_library'),
    #strona about_us
    path('about/', views.about_us, name='about_us'),
]