from django.shortcuts import render
from django.http import HttpResponse
from .models import Sneaker
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def sneakers_index(request):
  sneakers = Sneaker.objects.all()
  return render(request, 'sneakers/index.html', {'sneakers': sneakers})


def sneaker_details(request, sneaker_id):
  sneaker = Sneaker.objects.get(id = sneaker_id)
  return render(request, 'sneakers/details.html', {'sneaker': sneaker})

class SneakerCreate(CreateView):
  model = Sneaker
  fields = '__all__'

class SneakerUpdate(UpdateView):
  model = Sneaker
  fields = '__all__'

class SneakerDelete(DeleteView):
  model = Sneaker
  success_url = '/sneakers/'