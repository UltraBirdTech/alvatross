from django.test import TestCase

from django.contrib.auth.models import User
from ...models.post import Post
     
class PostTest(TestCase):
    def setUp(self):
        print('kiteru?')
        user = User.objects.create(
            username = 'test user'
        )
        self.post = Post.objects.create(
            title = 'test post',
            content = 'test content',
            status = 'active',
            user_id = user.id
        )
     
    def test_post_initialize(self):
        self.assertEqual(len(self.post.error_messages), 0)
        
    def test_post_str(self):
        self.assertEqual(self.post.__str__(), 'test post')
