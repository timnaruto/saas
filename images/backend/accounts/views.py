from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

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
    return render(request, 'home.html')





def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Change "home" to your actual redirect page
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "sign_in.html")


def register_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, "sign_up.html")