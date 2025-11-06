from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.FloatField()
    pubdate = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    available_copies = models.PositiveIntegerField(default=1)  # Liczba dostępnych egzemplarzy
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

def default_due_date():
    return timezone.now() + timedelta(days=30)

class BorrowedBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(default=timezone.now)
    return_due = models.DateTimeField(default=default_due_date)

    def __str__(self):
        return f"{self.user.username} → {self.book.name}"