from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class AuthenticationTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser")

    def test_user_created(self):
        user = User.objects.filter(username="testuser")
        self.assertTrue(user.exists())


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("register"))

    def test_register_get_request(self):
        self.assertEqual(self.response.status_code, 200)

    def test_register_post_request(self):
        form_data = {
            "username": "username",
            "password": "password",
            "password2": "password",
        }
        response = self.client.post(reverse("register"), form_data)
        self.assertEqual(response.status_code, 200)

    def test_register_correct_template(self):
        self.assertTemplateUsed(self.response, "accounts/register.html")


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="user", password="password")

    def test_logout(self):
        self.client.login(username="user", password="password")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
