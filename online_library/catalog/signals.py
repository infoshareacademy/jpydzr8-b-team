# catalog/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
from .models import BorrowedBook


@receiver(post_save, sender=BorrowedBook)
def send_borrow_notification(sender, instance, created, **kwargs):
    """Wysyła e-mail po utworzeniu nowego wypożyczenia"""

    if created:
        # Ustaw datę zwrotu na 30 dni po wypożyczeniu, jeśli brak
        if not instance.return_due:
            instance.return_due = instance.borrowed_at + timedelta(days=30)
            instance.save()

        book = instance.book
        user = instance.user

        # Pobierz autora (jeśli jest wielu — złącz przecinkiem)
        authors = ", ".join(a.name for a in book.authors.all()) or "(brak autora)"

        # Wyślij e-mail
        subject = "Confirmation of book loan 📚"
        message = f"""
Hi, {user.username},

You have just borrowed the book:

Title:  {book.name}
Author:  {authors}
Borrow date:  {instance.borrowed_at.strftime('%Y-%m-%d %H:%M')}
Return/subscription date:  {instance.return_due.strftime('%Y-%m-%d %H:%M')}

Best regards,
B-Team
        """

        send_mail(
            subject=subject,
            message=message.strip(),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

# # catalog/signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.apps import apps
# from .emails import send_borrow_notification
#
# MODEL_NAME = "BorrowedBook"
# APP_LABEL = "catalog"
#
# @receiver(post_save)
# def borrowedbook_post_save(sender, instance, created, **kwargs):
#     # filtrujemy tylko nasz model
#     if sender.__name__ != MODEL_NAME or sender._meta.app_label != APP_LABEL:
#         return
#
#     # tylko nowe rekordy
#     if not created:
#         return
#
#     # Pobieramy user i book z instancji (pola są 'user' i 'book' w Twoim modelu)
#     user_obj = getattr(instance, "user", None)
#     book_obj = getattr(instance, "book", None)
#
#     if not user_obj or not getattr(user_obj, "email", None):
#         # brak usera lub brak emaila — nic nie wysyłamy
#         return
#
#     try:
#         send_borrow_notification(user_obj, book_obj, instance)
#     except Exception as e:
#         # W produkcji: użyj logging zamiast print
#         print("Błąd wysyłania maila (borrowedbook_post_save):", e)