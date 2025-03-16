from django.shortcuts import render

# Create your views here.
def communications(request):
    return render(request, 'communications.html')
  