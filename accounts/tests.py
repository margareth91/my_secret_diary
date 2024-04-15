from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class AuthenticationTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser")

    def test_user_created(self):
        user = User.objects.filter(username="testuser")
        self.assertTrue(user.exists())


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="user", password="password")

    def test_logout(self):
        self.client.login(username="user", password="password")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
