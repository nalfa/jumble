from django.shortcuts import render, redirect
from .models import Word, Player
from .engine import get_objects
from django.contrib.auth.decorators import login_required
from .forms import PlayerForm
import json


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    bucket = Word.objects.values_list('text', 'hint')
    list_objects = get_objects(bucket)
    context = json.dumps(list_objects)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlayerForm(request.POST)
        # check whether it's valid:
    
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return redirect('pages:review')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlayerForm()

    return render(request, 'game/index.html', {'context': context, 'form': form})