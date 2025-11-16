
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from email.mime.image import MIMEImage
import uuid
import io

from .models import BorrowedBook

try:
    import qrcode

    QR_AVAILABLE = True
except Exception:
    QR_AVAILABLE = False


@receiver(post_save, sender=BorrowedBook)
def send_borrow_notification(sender, instance, created, **kwargs):
    """Wysyła e-mail po utworzeniu nowego wypożyczenia, dołączając unikalny QR"""

    # Wyślij tylko raz przy tworzeniu
    if not created or getattr(instance, '_email_sent', False):
        return

    # Ustaw datę zwrotu na 30 dni po wypożyczeniu, jeśli brak (bez save)
    if not instance.return_due:
        instance.return_due = instance.borrowed_at + timedelta(days=30)

    book = instance.book
    user = instance.user

    authors = ", ".join(a.name for a in book.authors.all()) or "(brak autora)"

    subject = "Confirmation of book loan 📚"
    text_message = f"""
Hi, {user.username},

You have just borrowed the book:

Title:  {book.name}
Author:  {authors}
Borrow date:  {instance.borrowed_at.strftime('%Y-%m-%d %H:%M')}
Return/subscription date:  {instance.return_due.strftime('%Y-%m-%d %H:%M')}

Best regards,
B-Team
    """.strip()

    if QR_AVAILABLE:
        unique_token = str(uuid.uuid4())
        qr_payload = f"borrow:{instance.pk};token:{unique_token}"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=6,
            border=2,
        )
        qr.add_data(qr_payload)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        bio = io.BytesIO()
        img.save(bio, format="PNG")
        bio.seek(0)
        qr_bytes = bio.read()

        cid = f"qr-{uuid.uuid4().hex}@bteam"
        html_message = f"""
        <html>
          <body>
            <p>Hi, {user.username},</p>
            <p>You have just borrowed the book:</p>
            <ul>
              <li><strong>Title:</strong> {book.name}</li>
              <li><strong>Author:</strong> {authors}</li>
              <li><strong>Borrow date:</strong> {instance.borrowed_at.strftime('%Y-%m-%d %H:%M')}</li>
              <li><strong>Return/subscription date:</strong> {instance.return_due.strftime('%Y-%m-%d %H:%M')}</li>
            </ul>

            <p><strong>Verification code:</strong> {unique_token}</p>

            <p>Scan the QR code to open your book:</p>
            <p><img src="cid:{cid}" alt="QR code" style="width:200px;height:200px;"/></p>

            <p>Best regards,<br/>B-Team</p>
          </body>
        </html>
        """

        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        msg.attach_alternative(html_message, "text/html")

        image = MIMEImage(qr_bytes, name="qrcode.png")
        image.add_header("Content-ID", f"<{cid}>")
        image.add_header("Content-Disposition", 'inline; filename="qrcode.png"')
        msg.attach(image)

        try:
            msg.send(fail_silently=False)
        except Exception:
            send_mail(
                subject=subject,
                message=text_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
    else:
        unique_token = str(uuid.uuid4())
        text_message_with_token = text_message + f"\n\nVerification code: {unique_token}"
        send_mail(
            subject=subject,
            message=text_message_with_token,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

    # ustaw flagę, aby uniknąć wysyłania drugi raz
    instance._email_sent = True
