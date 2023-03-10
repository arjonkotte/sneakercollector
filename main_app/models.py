from django.db import models
from django.urls import reverse

# Create your models here.

CLEAN_LEVELS = (
    ('B', 'Basic'),
    ('I', 'Intermediate'),
    ('D', 'Detailed')
)

CUSTOMIZATION_TYPES = (
    ('M', 'Maintenance'),
    ('S','Stylish'),
    ('P','Personal')
)

class Customization(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length = 1,
        choices = CUSTOMIZATION_TYPES,
        default = CUSTOMIZATION_TYPES[0][0]
    )

    def __str__(self):
        return f"{self.get_type_display()}"



class Sneaker(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)
    customizations = models.ManyToManyField(Customization)
    

    def __str__(self):
        return self.brand + ' ' + self.model

    def get_absolute_url(self):
        return reverse('details', kwargs={'sneaker_id': self.id})


class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    cleaning_level = models.CharField(
        max_length=1,
        choices=CLEAN_LEVELS,
        default=CLEAN_LEVELS[0][0]
    )

    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_cleaning_level_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for sneaker_id: {self.sneaker_id} @{self.url}"
