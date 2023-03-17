from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from post.models import Post

POSTS_URL = reverse('post:post-list')
ALL_POSTS_URL = reverse('post:all_posts')


class PublicPostsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(ALL_POSTS_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AuthorisedPostsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@vikas.com', name='Test Case', password='test1234'
        )
        self.client.force_authenticate(self.user)
    
    def test_create_post(self):
        payload = {
            "title": "titl3",
            "description": "Description3"
        }
        res = self.client.post(POSTS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_post_with_invalid_credentials(self):
        payload = {
            "description": "Description3"
        }
        res = self.client.post(POSTS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)