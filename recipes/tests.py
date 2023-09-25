from django.test import TestCase
from .models import Recipe, Ingredient
from .forms import RecipeForm
from django.urls import reverse


# Create your tests here.
class RecipeTestCase(TestCase):
    def setUp(self):
        # Set up any initial data needed for the tests
        self.ingredient1 = Ingredient.objects.create(name="Ingredient 1")

    def test_recipe_creation(self):
        # Test creating a new recipe
        recipe = Recipe.objects.create(
            title="Test Recipe",
            instructions="Test instructions",
        )
        recipe.ingredients.add(self.ingredient1)

        self.assertEqual(recipe.title, "Test Recipe")
        self.assertEqual(recipe.instructions, "Test instructions")
        self.assertIn(self.ingredient1, recipe.ingredients.all())

