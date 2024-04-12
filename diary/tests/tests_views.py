from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from diary.models import Entry


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get("")

    def test_get_index(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_correct_template(self):
        self.assertTemplateUsed(self.response, "diary/index.html")


class EntryListTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="user", password="password")

    def test_redirect_not_logged_user(self):
        response = self.client.get(reverse("entry_list"))
        self.assertEqual(response.status_code, 302)

    def test_get_entry_list_logged_user(self):
        self.client.login(username="user", password="password")
        response = self.client.get(reverse("entry_list"))
        self.assertEqual(response.status_code, 200)

    def test_entry_list_correct_template(self):
        self.client.login(username="user", password="password")
        response = self.client.get(reverse("entry_list"))
        self.assertTemplateUsed(response, "diary/entry_list.html")


class EntryDetailViewTest(TestCase):
    ENTRY_TITLE = "Lorem Ipsum"
    ENTRY_TEXT = "Lorem ipsum dolor sit amet."

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="user", password="password")
        Entry.objects.create(
            author=self.user, title=self.ENTRY_TITLE, text=self.ENTRY_TEXT
        )
        self.entry = Entry.objects.get(id=1)

    def redirect_not_logged_user(self):
        response = self.client.get(reverse("entry_detail"))
        self.assertEqual(response.status_code, 302)

    def get_entry_detail_logged_user(self):
        self.client.login(username="user", password="password")
        response = self.client.get(reverse("entry_detail"))
        self.assertEqual(response.status_code, 200)

    def test_entry_detail_correct_template(self):
        self.client.login(username="user", password="password")
        response = self.client.get(reverse("entry_detail", args=[1]))
        self.assertTemplateUsed(response, "diary/entry_detail.html")
