from django.contrib import admin

# Register your models here.
from .models import Word, Player

admin.site.register(Word)
admin.site.register(Player)
