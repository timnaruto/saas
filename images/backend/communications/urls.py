from django.urls import path
from . import views

urlpatterns = [
    path('', views.communications, name='communications'),
]