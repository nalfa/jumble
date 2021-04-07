from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BootstrapForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control col-sm-8'}),
            'email': forms.TextInput(attrs={'class': 'form-control col-sm-8 mb-4'}),
        }
        help_texts = {
            'username': None,
        }