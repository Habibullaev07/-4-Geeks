from django.urls import path
from main.views import banner

urlpatterns = [
    path('', banner, name='banner')
]
