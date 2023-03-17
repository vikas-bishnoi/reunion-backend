from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


REGISTER_URL = reverse('main:register')
AUTHENTICATE_URL = reverse('main:authenticate')
USER_URL = reverse('main:user')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserAPITests(TestCase):
    """these tests would not require authernications"""

    def setUp(self):
        self.client = APIClient()

