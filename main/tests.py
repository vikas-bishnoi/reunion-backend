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
    
    def test_create_valid_user_success(self):
        payload = {
            'email': 'test@vikas.com',
            'password': 'test1234',
            'name': 'Test Case'
        }
        res = self.client.post(REGISTER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(
            us.check_password(payload['password'])
        )
        self.assertNotIn('password', res.data)

    def test_create_valid_user_with_invalid_credentials(self):
        payload = {
            'email': 'test@vikas.com',
            'password': 'test1234',
        }
        res = self.client.post(REGISTER_URL, payload)
        self.assertEqual(res.status_code, 400)

    def test_user_already_exists(self):
        payload = {
            'email': 'test@vikas.com',
            'password': 'test1234',
            'name': 'Test Case'
        }
        create_user(**payload)
        res = self.client.post(REGISTER_URL, payload)
        self.assertTrue(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_login_user(self):
        payload = {
            'email': 'test@vikas.com',
            'password': 'test1234',
            'name': 'Test Case'
        }

        create_user(**payload)
        res = self.client.post(AUTHENTICATE_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_login_user_with_invalid_credentials(self):
        create_user(email='test@vikas.com', name='Test Case', password='test1234')
        payload = {
            'email': 'test@vikas.com',
            'password': 'test'
        }
        res = self.client.post(AUTHENTICATE_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)