from django.shortcuts import render

def main(request):
    """Main page."""
    return render(request, 'online_libraries/main.html')

def books_library(request):
    """Books library."""
    return render(request, 'online_libraries/books_library.html')

def about_us(request):
    """Books library."""
    return render(request, 'online_libraries/about_us.html')