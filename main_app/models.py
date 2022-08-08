from django.db import models

# Create your models here.

class Lego(models.Model):
    name = models.CharField(max_length=100)
    pieces = models.IntegerField()
    description = models.TextField(max_length=2500)
    minimumage = models.IntegerField()

def __str__(self):
    return f'{self.name} ({self.id})'