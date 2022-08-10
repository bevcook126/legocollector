from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Lego, Collection
from .forms import FigureForm

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
  id_list = lego.collections.all().values_list('id')
  unassociated_collections = Collection.objects.exclude(id__in=id_list)
  figure_form = FigureForm()
  return render(
    request, 
    'legos/detail.html', 
    {'lego': lego, 
    'figure_form': figure_form, 
    'collections': unassociated_collections
    }
  )

class LegoCreate(CreateView):
  model = Lego
  fields = '__all__'
  success_url = '/legos/'

class LegoUpdate(UpdateView):
  model = Lego
  fields = '__all__'

class LegoDelete(DeleteView):
  model = Lego
  success_url = '/legos/'

def add_figure(request, lego_id):
  form = FigureForm(request.POST)
  if form.is_valid():
    new_figure = form.save(commit=False)
    new_figure.lego_id = lego_id
    new_figure.save()
  return redirect('detail', lego_id=lego_id)

def assoc_collection(request, lego_id, collection_id):
  lego = Lego.objects.get(id=lego_id)
  lego.collections.add(collection_id)
  return redirect('detail', lego_id=lego_id)

def unassoc_collection(request, lego_id, collection_id):
  Lego.objects.get(id=lego_id).collections.remove(collection_id)
  return redirect('detail', lego_id=lego_id)

class CollectionList(ListView):
  model = Collection

class CollectionDetail(DetailView):
  model = Collection

class CollectionCreate(CreateView):
  model = Collection
  fields = '__all__'

class CollectionUpdate(UpdateView):
  model = Collection
  fields = ['name']

class CollectionDelete(DeleteView):
  model = Collection
  success_url = '/collections/'