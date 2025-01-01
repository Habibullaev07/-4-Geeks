from django.shortcuts import render
from apps.main.models import PhotoMain

# Create your views here.

def index(request):
    photo_main = PhotoMain.objects.all()
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html', locals())
