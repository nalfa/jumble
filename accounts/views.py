from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import BootstrapForm
from django.contrib.auth.models import User
from game.models import Player

# Create your views here.
def signupView(request):
    if request.method == 'POST':
        form = BootstrapForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pages:rules')
    else:
        form = BootstrapForm()
        
    return render(request, 'accounts/signup.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('pages:index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('pages:index')

@login_required(login_url='/login/')
def profileView(request, username):
    profile = User.objects.get(username=username)
    scores = Player.objects.filter(name__exact=username).order_by('-score')[:10]
    return render(request, 'accounts/profile.html', {'context': profile, 'scores': scores})
