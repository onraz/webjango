# conftest.py
import pytest
from django.contrib.auth.models import User

@pytest.fixture
def create_test_user():
    """Creates a standard test user."""
    user = User.objects.create_user(username='testuser', password='testpassword')
    return user

@pytest.fixture
def api_client():
   """A Django REST Framework API client instance."""
   from rest_framework.test import APIClient
   return APIClient()