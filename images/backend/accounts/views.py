from django.shortcuts import render
# accounts/views.py (or any app’s views.py)
from django.http import HttpResponse
from django.core.mail import send_mail

def send_test_email_view(request):
    try:
        send_mail(
            subject='Test Email',
            message='This is a test email from Django.',
            from_email='tosh75910@gmail.com',
            recipient_list=['kiptootitus75@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending email: {e}")


# Create your views here.
def home(request):
    return render(request, 'accounts.html')

