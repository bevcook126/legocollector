import os
import re
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lego, Collection, Photo
from .forms import MinifigForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def legos_index(request):
  legos = Lego.objects.filter(user=request.user)
  return render(request, 'legos/index.html', { 'legos': legos })

@login_required
def legos_detail(request, lego_id):
  lego = Lego.objects.get(id=lego_id)
  id_list = lego.collections.all().values_list('id')
  unassociated_collections = Collection.objects.exclude(id__in=id_list)
  minifig_form = MinifigForm()
  return render(
    request, 
    'legos/detail.html', 
    {'lego': lego, 
    'minifig_form': minifig_form, 
    'collections': unassociated_collections
    }
  )


class LegoCreate(CreateView, LoginRequiredMixin):
  model = Lego
  fields = ['name', 'pieces', 'availability', 'minimum_age']
  success_url = '/legos/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class LegoUpdate(UpdateView, LoginRequiredMixin):
  model = Lego
  fields = '__all__'


class LegoDelete(DeleteView, LoginRequiredMixin):
  model = Lego
  success_url = '/legos/'

@login_required
def add_minifig(request, lego_id):
  form = MinifigForm(request.POST)
  if form.is_valid():
    new_minifig = form.save(commit=False)
    new_minifig.lego_id = lego_id
    new_minifig.save()
  return redirect('detail', lego_id=lego_id)

@login_required
def assoc_collection(request, lego_id, collection_id):
  lego = Lego.objects.get(id=lego_id)
  lego.collections.add(collection_id)
  return redirect('detail', lego_id=lego_id)

@login_required
def unassoc_collection(request, lego_id, collection_id):
  Lego.objects.get(id=lego_id).collections.remove(collection_id)
  return redirect('detail', lego_id=lego_id)

@login_required
def add_photo(request, lego_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file: 
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, lego_id=lego_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', lego_id=lego_id)


class CollectionList(ListView, LoginRequiredMixin):
  model = Collection


class CollectionDetail(DetailView, LoginRequiredMixin):
  model = Collection


class CollectionCreate(CreateView, LoginRequiredMixin):
  model = Collection
  fields = '__all__'


class CollectionUpdate(UpdateView, LoginRequiredMixin):
  model = Collection
  fields = ['name']


class CollectionDelete(DeleteView, LoginRequiredMixin):
  model = Collection
  success_url = '/collections/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)