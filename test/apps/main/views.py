from django.http import HttpResponse
from django.shortcuts import render
from apps.main.models import Main

def index(request):
    main = Main.objects.latest('id')
    return render(request, 'index.html', locals())
