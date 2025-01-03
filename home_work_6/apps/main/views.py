from django.shortcuts import render
from apps.main.models import Main, Awards, About, AwardsBottom, Direction, Graduated

def index(request):
    main = Main.objects.latest('id')
    return render(request, 'index.html', locals())

def about(request):
    awards = Awards.objects.all()
    about = About.objects.latest('id')
    awards_bottom = AwardsBottom.objects.all()
    direction = Direction.objects.all()
    graduated = Graduated.objects.all()
    return render(request, 'about.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())
