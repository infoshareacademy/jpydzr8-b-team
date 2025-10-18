from django.shortcuts import render
from ol_project.logger_config import logger

def main(request):
    """Main page."""
    user_info = request.user.username if request.user.is_authenticated else "Anonymous"
    # logger.info(f"Użytkownik: {user_info} odwiedził strone 'Main Page' ")
    return render(request, 'online_library/main.html')

def books_library(request):
    """Books library."""
    user_info = request.user.username if request.user.is_authenticated else "Anonymous"
    return render(request, 'online_library/books_library.html')

def about_us(request):
    """About us page."""
    user_info = request.user.username if request.user.is_authenticated else "Anonymous"
    # logger.info(f"Użytkownik: {user_info} odwiedził stronę 'About Us'.")
    return render(request, 'online_library/about_us.html')
