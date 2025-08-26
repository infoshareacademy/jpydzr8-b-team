from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="accounts_details")
    city = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=50, blank=True)
    house_number = models.CharField(max_length=10, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    hobbies = models.TextField(max_length=500, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "User Details"

    def __str__(self):
        return f"{self.user.username} Details"
