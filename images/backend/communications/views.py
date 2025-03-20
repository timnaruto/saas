from django.shortcuts import render

# Create your views here.
def messages_view(request):
    return render(request, 'communications.html')
  