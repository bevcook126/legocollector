from django.forms import ModelForm
from .models import Figure

class FigureForm(ModelForm):
  class Meta:
    model = Figure
    fields = ['name']

