# Import necessary modules and classes
from django.shortcuts import render, redirect
from .forms import RecipeForm  # Importing the RecipeForm from forms.py
from .models import Ingredient, Recipe  # Importing models Ingredient and Recipe
from django.template import loader
from django.http import HttpResponse


# Define views for your recipe book application

# View for listing all recipes
def recipe_list(request):
    # Retrieve all Recipe objects from the database
    recipes = Recipe.objects.all()

    # Get the template 'recipe_list.html'
    template = loader.get_template('recipe_list.html')

    # Create a context dictionary to pass data to the template
    context = {
        'recipes': recipes
    }

    # Render the template with the context data and return as an HTTP response
    return HttpResponse(template.render(context, request))


# View for adding a new recipe
def add_recipe(request):
    # Get the template 'add_recipe.html'
    template = loader.get_template('add_recipe.html')

    if request.method == 'POST':
        # If the request method is POST, create a RecipeForm instance with POST data
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            # If the form is valid, save the form data to the database
            form.save()

            # Redirect to the 'recipe_list' view after successfully adding the recipe
            return redirect('recipe_list')
    else:
        # If the request method is not POST, create an empty RecipeForm instance
        form = RecipeForm()

    # Create a context dictionary to pass data to the template
    context = {
        'form': form,
    }

    # Render the template with the context data and return as an HTTP response
    return HttpResponse(template.render(context, request))


# View for searching for recipes
def search_recipe(request):
    # Get the search query from the GET request parameters
    query = request.GET.get('q')

    # Filter recipes whose title contains the search query
    recipes = Recipe.objects.filter(title__icontains=query)

    # Get the template 'recipe_list.html'
    template = loader.get_template('recipe_list.html')

    # Create a context dictionary to pass data to the template
    context = {
        'recipes': recipes,
    }

    # Render the template with the context data and return as an HTTP response
    return HttpResponse(template.render(context, request))
