"Definiuje wzorce adresow URL dla online_libraries"

from django.urls import path
from . import views

app_name = 'online_libraries'
urlpatterns = [
    #strona glowna
    path('', views.main, name='main'),
    # strona z baza ksiazek
    path('books_library/', views.books_library, name='books_library'),
    #strona about_us
    path('about_us/', views.about_us, name='about_us'),
]