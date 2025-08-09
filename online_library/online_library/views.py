from django.shortcuts import render

def main(request):
    """Main page."""
    return render(request, 'online_library/main.html')

def books_library(request):
    """Books library."""
    return render(request, 'online_library/books_library.html')

def about_us(request):
    """Books library."""
    return render(request, 'online_library/about_us.html')