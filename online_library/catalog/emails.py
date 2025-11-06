# catalog/emails.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_borrow_notification(user, book, borrow):
    """
    user: User instance (musi mieć .email)
    book: Book instance (powinien mieć .title, opcjonalnie .author)
    borrow: BorrowedBook instance (ma pola borrowed_at i return_due)
    """
    if not user or not getattr(user, "email", None):
        return False

    subject = f"Wypożyczono: {getattr(book, 'title', 'książka')}"
    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "biblioteka@example.com")
    to = [user.email]

    context = {
        "user": user,
        "book": book,
        "borrowed_at": getattr(borrow, "borrowed_at", ""),
        "return_due": getattr(borrow, "return_due", "")
    }

    text_body = render_to_string("emails/borrow_notification.txt", context)
    # Spróbuj załadować HTML, jeśli nie ma — EmailMultiAlternatives i tak zadziała z samym tekstem
    try:
        html_body = render_to_string("emails/borrow_notification.html", context)
    except Exception:
        html_body = None

    msg = EmailMultiAlternatives(subject, text_body, from_email, to)
    if html_body:
        msg.attach_alternative(html_body, "text/html")
    msg.send(fail_silently=False)
    return True