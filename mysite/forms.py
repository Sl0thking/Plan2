from django import forms
from foodplan.models import Ingredient 
 
class recipeForm(forms.Form):
    name = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)
    ingredients = forms.MultipleChoiceField()