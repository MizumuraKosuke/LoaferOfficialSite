from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            subject = post.name + 'さんからホームページに新しいメッセージが届きました。'
            message = 'NAME: ' + post.name + '\n' + 'mail adress: ' + post.mail_address + '\n\n'+ 'Message: ' + post.message
            from_email = post.mail_address
            to = [
                settings.EMAIL_HOST_USER,
            ]
            send_mail(subject, message, from_email, to)
            return redirect(contact)
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})