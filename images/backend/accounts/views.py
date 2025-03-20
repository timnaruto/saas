from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


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
        username = request.POST.get("username", "").strip()
        fname = request.POST.get("fname", "").strip()
        lname = request.POST.get("lname", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        password2 = request.POST.get("password2", "").strip()

        if not username or not fname or not lname or not email or not password or not password2:
            messages.error(request, "All fields are required.")
            return redirect("register")  # Redirect back to registration page

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect("register")

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=fname,
                last_name=lname
            )
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("home")
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
            return redirect("register")

    return render(request, "sign_up.html")
