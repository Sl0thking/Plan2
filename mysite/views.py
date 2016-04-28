import os
import sys
from django.http import HttpResponse
from django.template import Template, Context
from foodplan.models import Recipe

def hello(request):
    rec = Recipe()
    rec.name = "Test"
    rec.save()
    return HttpResponse("<HTML>Hallo</HTML>")

def showRecipes(request):
    fp = open('.\\htmlTemplates\\recipeOverview.html')
    t = Template(fp.read())
    fp.close()
    recipes = Recipe.objects.all()
    html = t.render(Context({'recipes': recipes}))
    return HttpResponse(html)