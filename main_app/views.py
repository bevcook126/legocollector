from django.shortcuts import render
from .models import Lego

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def legos_index(request):
  legos = Lego.objects.all()
  return render(request, 'legos/index.html', { 
  'legos': legos 
  })

def legos_detail(request, lego_id):
  lego = Lego.objects.get(id=lego_id)
  return render(request, 'legos/detail.html', {'lego': lego})