# Import the necessary module for defining Django models
from django.db import models


# Define a Django model called Ingredient
class Ingredient(models.Model):
    # Define a field 'name' for the ingredient with a maximum length of 255 characters
    name = models.CharField(max_length=255)

    # Define a method '__str__' to represent the ingredient as a string
    def __str__(self):
        return self.name  # Return the name of the ingredient when it's converted to a string


# Define another Django model called Recipe
class Recipe(models.Model):
    # Define a field 'title' for the recipe with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # Define a Many-to-Many relationship with the Ingredient model, allowing multiple ingredients for a recipe
    # The 'related_name' attribute allows you to access recipes associated with an ingredient using 'recipes'
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    # Define a field 'instructions' for the recipe as a large text field
    instructions = models.TextField()

    # Define an 'image' field for the recipe, which allows you to upload an image
    # The 'upload_to' attribute specifies the directory where uploaded images will be stored
    # Images will be stored in a directory named 'recipe/' within your media root
    image = models.ImageField(upload_to='recipe/')

    # Define a method '__str__' to represent the recipe as a string
    def __str__(self):
        return self.title  # Return the title of the recipe when it's converted to a string
