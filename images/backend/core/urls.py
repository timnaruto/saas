from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('api/', include('communications.urls')),
    path('accounts/', include('allauth.urls')),

]
