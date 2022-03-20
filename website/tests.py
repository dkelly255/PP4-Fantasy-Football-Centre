from django.test import TestCase
from .models import Comment
from django.contrib.auth.models import User
from .models import Post
# Create your tests here.


class TestViews(TestCase):

    def test_view_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')

    def test_view_post_list(self):
        response = self.client.get('/post-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_post_detail(self):
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        self.client.login(username='testuser', password='testpw')
        article = Post.objects.create(
            title='test article', 
            slug='test-article',
            author=test_user
            content='test content',                        
            created_on=''
        )
        self.assertEqual(featured_image, 'placeholder') 


# class TestModels(TestCase):

#     def test_approved_defaults_to_false(self):
#         comment = Comment.objects.create(name="Test Comment")
#         self.assertFalse(comment.approved)