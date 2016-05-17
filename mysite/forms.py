from django import forms
from foodplan.models import Ingredient 
 
class recipeForm(forms.Form):
    name = forms.CharField(required=False)
    desc = forms.CharField(required=False, widget=forms.Textarea)
    
class ingredientForm(forms.Form):
    ingredientName = forms.CharField(required=True)
    ingredientQuantity = forms.IntegerField(required=True)
    ingrednientType = forms.CheckboxInput()