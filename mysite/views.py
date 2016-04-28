import os
import sys
from django.http import HttpResponse
from foodplan.models import Recipe

def hello(request):
    rec = Recipe()
    rec.name = "Test"
    rec.save()
    return HttpResponse("<HTML>Hallo</HTML>")

