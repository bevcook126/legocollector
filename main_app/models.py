from django.db import models
from django.urls import reverse

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('collections_detail', kwargs={'pk': self.id})

class Lego(models.Model):
    name = models.CharField(max_length=100)
    pieces = models.IntegerField()
    availability = models.TextField(max_length=2500)
    minimum_age = models.IntegerField()
    collections = models.ManyToManyField(Collection)


    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'lego_id': self.id})

class Figure(models.Model):
    name = models.CharField(max_length=100)
    lego = models.ForeignKey(
        Lego,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Added {self.name} to {self.lego}'

