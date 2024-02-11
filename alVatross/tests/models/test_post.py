from django.test import TestCase

from django.contrib.auth.models import User
from ...models.post import Post
     
class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'test user'
        )
        self.title = 'test title'
        self.content = 'test content'
        self.status = 'active'
        self.create_post()

    def create_post(self):
        self.post = Post.objects.create(
            title = self.title,
            content = self.content,
            status = self.status,
            user_id = self.user.id
        )
     
    def test_post_initialize(self):
        self.assertEqual(len(self.post.error_messages), 0)
        
    def test_post_str(self):
        self.assertEqual(self.post.__str__(), 'test title')

    def test_post_clean_title_99_str(self):
        self.title = 't' * 99
        self.create_post()
        self.post.clean_title()
        self.assertEqual(len(self.post.error_messages), 0)

    def test_post_clean_title_100_str(self):
        self.title = 't' * 100
        self.create_post()
        self.post.clean_title()
        self.assertEqual(len(self.post.error_messages), 0)

    def test_post_clean_title_101_str(self):
        self.title = 't' * 101
        self.create_post()
        self.post.clean_title()
        self.assertEqual(len(self.post.error_messages), 1)
        self.assertEqual(self.post.error_messages[0], 'タイトルの文字数が100文字を超えています')

    def test_post_clean_content_4999_str(self):
        self.content = 'c' * 4999 
        self.create_post()
        self.post.clean_content()
        self.assertEqual(len(self.post.error_messages), 0)

    def test_post_clean_content_5000_str(self):
        self.content = 'c' * 5000 
        self.create_post()
        self.post.clean_content()
        self.assertEqual(len(self.post.error_messages), 0)

    def test_post_clean_content_5001_str(self):
        self.content = 'c' * 5001
        self.create_post()
        self.post.clean_content()
        self.assertEqual(len(self.post.error_messages), 1)
        self.assertEqual(self.post.error_messages[0], 'コンテンツの文字数が5000文字を超えています')

    def test_post_clean_status_active(self):
        self.create_post()
        self.post.clean_status()
        self.assertEqual(len(self.post.error_messages), 0)

    def test_post_clean_status_delete(self):
        self.status = 'delete'
        self.create_post()
        self.post.clean_status()
        self.assertEqual(len(self.post.error_messages), 0)

    def test_post_clean_status_other_string(self):
        self.status = 'other string'
        self.create_post()
        self.post.clean_status()
        self.assertEqual(len(self.post.error_messages), 1)
        self.assertEqual(self.post.error_messages[0], 'ステータスに規定外の文字列が入力されています')


