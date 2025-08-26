from django.db import models

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

    def __str__(self):
        return self.name

