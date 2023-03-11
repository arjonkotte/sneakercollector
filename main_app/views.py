from .models import Sneaker, Photo
import boto3
import uuid
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sneaker
from .forms import CleaningForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'sneakercollec'

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def sneakers_index(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'sneakers/index.html', {'sneakers': sneakers})


def sneaker_details(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    cleaning_form = CleaningForm()
    return render(request, 'sneakers/details.html', {'sneaker': sneaker, 'cleaning_form': cleaning_form})


class SneakerCreate(CreateView):
    model = Sneaker
    fields = '__all__'


class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = '__all__'


class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'

def add_cleaning(request, sneaker_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.sneaker_id = sneaker_id
        new_cleaning.save()
    return redirect('details', sneaker_id=sneaker_id)


def add_photo(request, sneaker_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = 'sneakercollec/' + \
            uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, sneaker_id=sneaker_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('details', sneaker_id=sneaker_id)
