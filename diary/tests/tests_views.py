from django.test import TestCase, Client


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get("")

    def test_get_index(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_correct_template(self):
        self.assertTemplateUsed(self.response, "diary/index.html")
