from django.urls import path
from apps.main.views import index, about, contact

urlpatterns = [
    path('', index, name='index'),  
    path('about.html', about, name='about'),
    path('contact.html', contact, name='contact'),
]

