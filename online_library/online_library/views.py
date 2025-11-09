from django.shortcuts import render
from ol_project.logger_config import logger
from catalog.models import Book
from django.utils.translation import gettext_lazy as _


def main(request):
    """Main page."""
    user_info = request.user.username if request.user.is_authenticated else "Anonymous"
    logger.info(f"Użytkownik: {user_info} odwiedził strone 'Main Page' ")
    return render(request, 'online_library/main.html')


def books_library(request):
    """Books library."""
    user_info = request.user.username if request.user.is_authenticated else "Anonymous"
    return render(request, 'online_library/books_library.html')


def about_us(request):
    """About us page."""
    user_info = request.user.username if request.user.is_authenticated else "Anonymous"
    logger.info(f"Użytkownik: {user_info} odwiedził stronę 'About Us'.")
    return render(request, 'online_library/about_us.html')



# WYSZUKIWARKA
def searcher(request):

    # List of Category tuples
    # value is translated,
    # slug no, because is filtered in database-table (written in english)
    categories = [
        ('-', '-'),
        ('novel', _('novel')),
        ('drama', _('drama')),
        ('comedy', _('comedy')),
        ('romance', _('romance')),
        ('diary', _('diary')),
        ('science fiction', _('science fiction')),
        ('fantasy', _('fantasy')),
    ]

    # Params from GET
    query = request.GET.get('q', '').strip()
    filter_value = request.GET.get('optselect', '')
    selected_category_index = request.GET.get('category', '0')

    # Give me 0 when there is no user-choice
    try:
        selected_category_index = int(selected_category_index)
    except ValueError:
        selected_category_index = 0

    # Retrives slug index, by value
    selected_category = categories[selected_category_index][0] if selected_category_index > 0 else ''

    books = Book.objects.all()

    if query:
        if filter_value == 'name':
            books = books.filter(name__icontains=query)
        elif filter_value == 'author':
            books = books.filter(authors__name__icontains=query)
        elif selected_category:
            books = books.filter(category__icontains=selected_category)
        else:
            # defaultly searching by title or author when a phrase exists, and no filter
            books = books.filter(name__icontains=query) | Book.objects.filter(authors__name__icontains=query)
    elif selected_category:
        books = books.filter(category__icontains=selected_category)
    else:
        books = Book.objects.none()


    context = {
        'query': query,
        'categories': [(i, name) for i, (_, name) in enumerate(categories)],
        'selected_category': selected_category_index,
        'results': books.distinct(),
        'filter_value': filter_value,
    }
    return render(request, 'online_library/search.html', context)