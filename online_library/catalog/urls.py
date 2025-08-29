from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('library/', views.books_library, name='books_library'),
    path('library/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('my-books/', views.my_books, name='my_books'),
    path('my-books/return/<int:book_id>/', views.return_book, name='return_book'),
]
