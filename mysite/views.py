import os
import sys
import re
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from foodplan.models import Recipe, Ingredient
from mysite.forms import recipeForm
from django.http.response import HttpResponseRedirect

def hello(request):
    rec = Recipe()
    rec.name = "Wasser"
    rec.save()
    
    ingre = Ingredient()
    ingre.name = "Wasser"
    ingre.quantityInMl = 250;
    ingre.save()

    ingre2 = Ingredient()
    ingre2.name = "Noch mehr Wasser"
    ingre2.quantityInMl = 350;
    ingre2.save()
    
    rec.ingredients.add(ingre);
    rec.ingredients.add(ingre2);
    rec.save()
    return HttpResponse("<HTML>Hallo</HTML>")

def showRecipes(request):
    fp = open('.\\htmlTemplates\\recipeOverview.html')
    t = Template(fp.read())
    fp.close()
    recipes = Recipe.objects.all()
    html = t.render(Context({'recipes': recipes}))
    return HttpResponse(html)

def showRecipeForm(request):
    form = recipeForm(request.POST)
    return render(request, 'recipeAdd.html', {'form': form})
    
def showRecipeDetails(request):
    rec = Recipe()
    rec.
    return render(request, '')
    
def addRecipe(request):
    rec = Recipe()
    form = recipeForm(request.POST)
    ingredientForm = ingredientForm(request.POST)
    rec.name = request.POST['name']
    rec.description = request.POST['desc']
    rec.save()
    return HttpResponseRedirect("recipeDetails.html?rip=" + rec.id)