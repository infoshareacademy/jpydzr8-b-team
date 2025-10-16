from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, BorrowedBook
from ol_project.logger_config import logger


def books_library(request):
    books = Book.objects.all()
    logger.info(f"Użytkownik {request.user.username} odwiedził strone 'Library' ")
    return render(request, 'online_library/books_library.html', {'books': books})


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Sprawdzenie, ile książek już wypożyczył użytkownik
    borrowed_count = BorrowedBook.objects.filter(user=request.user).count()
    if borrowed_count >= 5:
        messages.error(request, "You cannot borrow more than 5 books at the same time.")
        logger.warning(f"User '{request.user.username}' tried to borrow more than 5 books.")
        return redirect('catalog:books_library')
    # Sprawdzamy, czy użytkownik już wypożyczył tę książkę
    already_borrowed = BorrowedBook.objects.filter(user=request.user, book=book).exists()
    if already_borrowed:
        messages.error(request, f'You have already borrowed "{book.name}".')
        logger.warning(f"User '{request.user.username}' tried to borrow book '{book.name}' again.")
        return redirect('catalog:books_library')

    if book.available_copies > 0:
        book.available_copies -= 1
        book.save()

        BorrowedBook.objects.create(user=request.user, book=book)

        messages.success(request, f'You have successfully borrowed "{book.name}".')
        logger.info(f"User '{request.user.username}' borrowed book '{book.name}'.")
    else:
        messages.error(request, f'"{book.name}" is not available at the moment.')
        logger.warning(f"User '{request.user.username}' tried to borrow unavailable book '{book.name}'.")

    return redirect('catalog:books_library')

@login_required
def my_books(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return render(request, 'catalog/my_books.html', {'borrowed_books': borrowed_books})


@login_required
def return_book(request, book_id):
    if request.method != "POST":
        messages.error(request, "Invalid request method.")
        return redirect('catalog:my_books')
    # Pobieramy rekord wypożyczenia
    borrowed_book = BorrowedBook.objects.filter(user=request.user, book_id=book_id).first()

    if not borrowed_book:
        messages.error(request, "You haven't borrowed this book.")
        return redirect('catalog:my_books')

    # Zwiększamy liczbę dostępnych kopii
    book = borrowed_book.book
    book.available_copies += 1
    book.save()

    # Usuwamy rekord wypożyczenia
    borrowed_book.delete()

    messages.success(request, f'You have successfully returned "{book.name}".')
    logger.info(f"User '{request.user.username}' returned book '{book.name}'.")
    return redirect('catalog:my_books')


