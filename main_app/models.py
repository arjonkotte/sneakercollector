from django.db import models

# Create your models here.
# Add the Cat class & list and view function below the imports
class Sneaker(models.Model):  # Note that parens are optional if not inheriting from another class
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.brand + ' ' + self.model

# sneakers = [
#   Sneaker('Nike', 'AirForce 1', 2021, 'White with black logo and sole'),
#   Sneaker('Nike', 'Jordan 5 Retro Top 3', 2020, 'Black with blue accents'),
#   Sneaker('Puma', 'Pokemon Pikachu', 2022, 'Pikachu Yellow with white & red accents')
# ]