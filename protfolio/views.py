from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)

def send_email_via_sendgrid(subject, message, from_email, to_emails):
    """Send email using SendGrid API directly"""
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    
    sg_message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        plain_text_content=message
    )
    
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    response = sg.send(sg_message)
    return response

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # 2. Get the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"New Portfolio Message from {name}"
            email_message = f"You received a new message:\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # If email credentials are missing, inform the user instead of throwing.
            if not settings.EMAIL_HOST_USER or (not settings.EMAIL_HOST_PASSWORD and not getattr(settings, 'SENDGRID_API_KEY', None)):
                logger.error("Email credentials are missing!")
                logger.error(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
                logger.error(f"EMAIL_HOST_PASSWORD exists: {bool(settings.EMAIL_HOST_PASSWORD)}")
                logger.error(f"SENDGRID_API_KEY exists: {bool(getattr(settings, 'SENDGRID_API_KEY', None))}")
                messages.error(request, 'Messaging is not available right now. Please try again later.')
                return redirect('index')

            try:
                logger.info(f"Attempting to send email from {settings.DEFAULT_FROM_EMAIL}")
                
                # Use SendGrid if API key is available, otherwise use SMTP
                if getattr(settings, 'SENDGRID_API_KEY', None):
                    logger.info("Using SendGrid API")
                    send_email_via_sendgrid(
                        subject,
                        email_message,
                        settings.DEFAULT_FROM_EMAIL,
                        ['hardikmittal230407@gmail.com']
                    )
                else:
                    logger.info("Using SMTP")
                    send_mail(
                        subject,
                        email_message,
                        settings.DEFAULT_FROM_EMAIL,
                        ['hardikmittal230407@gmail.com'],
                        fail_silently=False,
                    )
                
                logger.info("Email sent successfully!")
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as exc:
                logger.error(f"Error sending email: {exc}", exc_info=True)
                messages.error(request, 'Messaging is not available right now. Please try again later.')

            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})