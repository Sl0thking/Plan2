from django import forms
from foodplan.models import Ingredient 
 
class RecipeForm(forms.Form):
    name = forms.CharField(required=False)
    desc = forms.CharField(required=False, widget=forms.Textarea)

class IngredientForm(forms.Form):
    
    IMP_CHOICES = (("1", "Ml"), ("2", "Mg"), ("3", "Nr"))
    
    ingredientName = forms.CharField(required=True)
    ingredientQuantity = forms.IntegerField(required=True)
    ingredientType = forms.ChoiceField(choices=IMP_CHOICES)