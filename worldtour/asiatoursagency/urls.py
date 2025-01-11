from django.urls import path
from . import views

# Define a list of URL patterns
urlpatterns = [
    # Define the URL pattern for the index view
    path('', views.index),
]