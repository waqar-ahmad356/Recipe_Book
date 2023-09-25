# Import necessary modules and functions from Django
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Define the URL patterns for your Django application
urlpatterns = [
    # URL pattern for the recipe list view (e.g., displaying all recipes)
    path('', views.recipe_list, name='recipe_list'),

    # URL pattern for the add recipe view (e.g., for creating new recipes)
    path('add/', views.add_recipe, name='add_recipe'),

    # URL pattern for the search recipe view (e.g., searching for recipes)
    path('search/', views.search_recipe, name='search_recipe'),
]

# This line is used to serve media files (e.g., uploaded images) during development.
# It appends a URL pattern for serving media files to the existing urlpatterns.
# This is done using the static() function, which maps a URL to a directory where
# media files are stored (settings.MEDIA_ROOT).
# settings.MEDIA_URL represents the URL prefix for serving media files, and
# settings.MEDIA_ROOT represents the filesystem path where media files are stored.
# This configuration is useful for local development but should be handled differently
# in production for better security and performance.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
