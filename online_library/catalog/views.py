from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book


def books_library(request):
    books = Book.objects.all()
    return render(request, 'online_library/books_library.html', {'books': books})


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.available_copies > 0:
        book.available_copies -= 1
        book.save()
        messages.success(request, f'You have successfully borrowed "{book.name}".')
    else:
        messages.error(request, f'"{book.name}" is not available at the moment.')

    return redirect('catalog:books_library')
