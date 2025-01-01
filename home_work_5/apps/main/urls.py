from django.urls import path
from apps.main.views import index, about

urlpatterns = [
    path('', index, name='index'),  
    path('about.html', about, name='about')
]
