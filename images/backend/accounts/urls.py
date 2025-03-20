from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
path('test-email/', views.send_test_email_view, name='send_test_email'),

]
