from django.db import models

# Create your models here.
class Word(models.Model):
    text = models.CharField(max_length=5)
    hint = models.CharField(max_length=50)

    def __str__(self):
        return self.text


class Player(models.Model):
    name = models.CharField(max_length=150)
    score = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

