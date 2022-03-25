from django.test import TestCase
from .models import Comment
from django.contrib.auth.models import User
from .models import Article
# Create your tests here.


class TestViews(TestCase):

    def test_view_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')

    def test_view_article_list(self):
        response = self.client.get('/article-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
