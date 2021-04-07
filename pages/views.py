from django.shortcuts import render, redirect
from game.models import Player
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    bucket = []
    check = []
    for i in Player.objects.all().order_by('-score'):
        if i.name not in check:
            bucket.append(i)
            check.append(i.name)
    return render(request, 'pages/index.html', {'context': bucket[:5]})

def leaderboard(request):
    bucket = []
    check = []
    for i in Player.objects.all().order_by('-score'):
        if i.name not in check:
            bucket.append(i)
            check.append(i.name)
    return render(request, 'pages/leaderboard.html', {'context': bucket[:25]})

@login_required(login_url='/login/')
def review(request):
    stats = Player.objects.filter(name__exact=request.user.username).last()
    return render(request, 'pages/review.html', {'context': stats})

@login_required(login_url='/login/')
def rules(request):
    return render(request, 'pages/rules.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:index')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})

