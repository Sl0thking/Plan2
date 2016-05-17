from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=60)
    quantityInMl = models.IntegerField(null=True)
    quantityInMg = models.IntegerField(null=True)
    quantityInNr = models.IntegerField(null=True)
    
    def __str__(self):
        return name

class Recipe(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)
    ingredients = models.ManyToManyField(Ingredient)

class Day(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateField()
    breakfast = models.ForeignKey(Recipe, null=True, related_name='breakfast')
    lunch = models.ForeignKey(Recipe, null=True, related_name='lunch')
    dinner = models.ForeignKey(Recipe, null=True, related_name='dinner')