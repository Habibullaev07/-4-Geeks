from django.shortcuts import render
from main.models import Banner

# Create your views here.

def banner(request):
    banners = Banner.objects.all()
    return render(request, 'index.html', locals())

