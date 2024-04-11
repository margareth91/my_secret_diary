import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from diary.models import Entry


class EntryModelTest(TestCase):
    ENTRY_TITLE = "Lorem Ipsum"
    ENTRY_TEXT = "Lorem ipsum dolor sit amet."

    def setUp(self):
        self.author = User.objects.create()
        Entry.objects.create(
            author=self.author, title=self.ENTRY_TITLE, text=self.ENTRY_TEXT
        )
        self.entry = Entry.objects.get(id=1)

    def test_entry_author(self):
        self.assertTrue(self.entry.author, self.author)

    def test_entry_title(self):
        self.assertEqual(self.entry.title, self.ENTRY_TITLE)

    def test_entry_text(self):
        self.assertEqual(self.entry.text, self.ENTRY_TEXT)

    def test_date_added_automatically(self):
        self.assertTrue(type(self.entry.created_date), datetime)

    def test_verbose_name_plural(self):
        verbose_name_plural = self.entry._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "entries")

    def test_str(self):
        self.assertEqual(self.entry.__str__(), self.entry.title)
