from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=60)
    quantity = models.IntegerField(null=True)
    
    
class Recipe(models.Model):
    name = models.CharField(max_length=60)
    ingredients = models.ManyToManyField(Ingredient)