from django.db import models
from django.urls import reverse

# Create your models here.

class Sneaker(models.Model):  
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.brand + ' ' + self.model
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'sneaker_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for sneaker_id: {self.sneaker_id} @{self.url}"
