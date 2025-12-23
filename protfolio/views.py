from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

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
            
            try:
                send_mail(
                    subject,
                    email_message,
                    settings.EMAIL_HOST_USER,
                    ['mittalhardik2007@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as exc:
                print(f"Error sending email: {exc}")
                messages.error(request, 'Messaging is not available right now. Please try again later.')

            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})