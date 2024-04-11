from django.test import TestCase, Client


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_index(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
