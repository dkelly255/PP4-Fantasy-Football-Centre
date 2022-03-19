from django.test import TestCase

# Create your tests here.


class TestDjango(TestCase):

    def test_view_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')
