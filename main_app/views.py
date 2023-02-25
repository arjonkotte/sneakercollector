from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Add the Cat class & list and view function below the imports
class Sneaker:  # Note that parens are optional if not inheriting from another class
  def __init__(self, brand, model, year, description):
    self.brand = brand
    self.model = model
    self.year = year
    self.description = description

sneakers = [
  Sneaker('Nike', 'AirForce 1', '2021', 'White with black logo and sole'),
  Sneaker('Nike', 'Jordan 5 Retro Top 3', '2020', 'Black with blue accents'),
  Sneaker('Puma', 'Pokemon Pikachu', '2022', 'Pikachu Yellow with white & red accents')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def sneakers_index(request):
    return render(request, 'sneakers/index.html', { 'sneakers': sneakers})