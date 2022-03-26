from django.test import TestCase
from .models import Comment
from django.contrib.auth.models import User
from .models import Article
# Create your tests here.

# Credits: I gained the idea for testing these views from the 
# CI "Hello Django Blog" testing exercises

class TestViews(TestCase):

    def test_view_landing_page(self):
        """
        The Landing Page view loads the correct template
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')

    def test_view_article_list(self):
        """
        The Article List view loads the correct template
        """
        response = self.client.get('/article-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
