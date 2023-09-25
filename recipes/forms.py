# Import necessary modules
from django import forms
from .models import Recipe

# Define a ModelForm called RecipeForm
class RecipeForm(forms.ModelForm):
    class Meta:
        # Specify the model that this form is associated with
        model = Recipe

        # Define the fields that should be included in the form
        fields = ['title', 'ingredients', 'instructions', 'image']
