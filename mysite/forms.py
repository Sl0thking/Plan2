from django import forms
from foodplan.models import Ingredient 
 
class recipeForm(forms.Form):
    name = forms.CharField(required=False)
    desc = forms.CharField(required=False, widget=forms.Textarea)