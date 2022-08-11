from django.forms import ModelForm
from .models import Minifig

class MinifigForm(ModelForm):
  class Meta:
    model = Minifig
    fields = ['name', 'accessories']

