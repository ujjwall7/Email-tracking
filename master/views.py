from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from . models import SentEmail
from django.urls import reverse



def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        to_email = request.POST.get('to')
        message = request.POST.get('message')

        # Generate the URL for marking email as opened
        email = SentEmail(subject=subject, to_email=to_email, message=message)
        email.save()
        url = request.build_absolute_uri(reverse('mark_email_as_opened', args=[email.id]))

        # Include the URL in the email message
        email_message = f"Please click the following link to mark the email verification: {url}"
        send_mail(subject, email_message, settings.EMAIL_HOST_USER, [to_email])

        return render(request, 'email_sent.html')

    return render(request, 'email_form.html')


def mark_email_as_opened(request, email_id):
    try:
        email = SentEmail.objects.get(pk=email_id)
    except SentEmail.DoesNotExist:
        return render(request, 'email_not_found.html')

    # Update the is_opened field to True
    email.is_opened = True
    email.save()

    return render(request, 'email_opened.html')