# App_UTG/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),  # Root URL
    path('generate/', views.generate_tests, name='generate_tests'),  # Endpoint for generating tests
]
