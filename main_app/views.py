from django.shortcuts import render
from django.http import HttpResponse
from .models import Sneaker

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def sneakers_index(request):
  sneakers = Sneaker.objects.all()
  return render(request, 'sneakers/index.html', { 'sneakers': sneakers})

def sneaker_details(request, sneaker_id):
  sneaker = Sneaker.objects.get(id = sneaker_id)
  return render(request, 'sneakers/details.html', { 'sneaker': sneaker})