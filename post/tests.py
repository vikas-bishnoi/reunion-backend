from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

ALL_POSTS_URL = reverse('post:all_posts')

class PublicPostsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(ALL_POSTS_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)