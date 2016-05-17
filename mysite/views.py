import os
import sys
import re
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from foodplan.models import Recipe, Ingredient
from mysite.forms import RecipeForm, IngredientForm
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
    form = RecipeForm(request.POST)
    return render(request, 'recipeAdd.html', {'form': form})
    
def showRecipeDetails(request):
    rec_id = request.GET["id"]
    rec = Recipe.objects.get(id=rec_id)
    form = RecipeForm({'name':rec.name, 'desc':rec.description})
    ingredientForm = IngredientForm()
    return render(request, 'recipeDetails.html', {'form': form, 'ingredientForm': ingredientForm, 'recipe': rec})
    
def addIngredient(request):
    recNr = request.GET['recId']
    ingredient = Ingredient()
    ingredient.name = request.POST['ingredientName']
    if request.POST['ingredientType'] == "1":
        ingredient.quantityInMl = request.POST['ingredientQuantity']
        ingredient.quantityInMg = 0
        ingredient.quantityInNr = 0
    elif request.POST['ingredientType'] == "2":
        ingredient.quantityInMl = 0
        ingredient.quantityInMg = request.POST['ingredientQuantity']
        ingredient.quantityInNr = 0
    else:
        ingredient.quantityInMl = 0
        ingredient.quantityInMg = 0
        ingredient.quantityInNr = request.POST['ingredientQuantity']
    ingredient.save()
    rec = Recipe.objects.get(id=recNr)
    rec.ingredients.add(ingredient)
    rec.save()
    return HttpResponseRedirect("/recipeDetails/?id=" + str(rec.id))
    
def delIngredient(request):
    ingreId = request.GET['ingreId']
    recId = request.GET['recId']
    Ingredient.objects.filter(id=ingreId).delete()
    return HttpResponseRedirect("/recipeDetails/?id=" + str(recId))
    
def addRecipe(request):
    rec = Recipe()
    rec.name = request.POST['name']
    rec.description = request.POST['desc']
    rec.save()
    return HttpResponseRedirect("/recipeDetails/?id=" + str(rec.id))

def delRecipe(request):
    recId = request.GET['recId']
    Recipe.objects.filter(id=recId).delete()
    return HttpResponseRedirect("/showRecipes/")