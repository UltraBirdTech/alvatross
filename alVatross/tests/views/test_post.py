from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from ...models.post import Post

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'test_user'
        )
        self.client = Client()
        self.client.force_login(self.user)

        print('*' * 100)
        print(self.user)
        print(self.user.id)
        print('*' * 100)
        self.post = Post.objects.create(
            title = 'test post',
            content = 'test content',
            status = 'active',
            user_id = self.user.id
        )

        self.params = {
            'title': 'test post',
            'content': 'test content',
            'status': 'active',
            'user_id' : self.user.id,
            'redirect_url': '/alvatross/post'
        }

    ########################################
    # test post list.
    ########################################
    def test_initialize(self):
        response = self.client.get('/alVatross/post/')
        self.assertEqual(response.status_code, 200)

    ########################################
    # test post insert.
    ########################################
    def test_initialize_post_insert(self):
        response = self.client.get('/alVatross/post/insert')
        self.assertEqual(response.status_code, 200)

    def test_post_insert(self):
        response = self.client.post('/alVatross/post/insert', self.params)
        self.assertEqual(response.status_code, 302)

    def test_post_insert_success_title_99_char(self):
        self.params['title'] = 't' * 99
        response = self.client.post('/alVatross/post/insert', self.params)
        self.assertEqual(response.status_code, 302)

    def test_post_insert_success_title_100_char(self):
        self.params['title'] = 't' * 100
        response = self.client.post('/alVatross/post/insert', self.params)
        self.assertEqual(response.status_code, 302)

    def test_post_insert_invalid_title_101_char(self):
        self.params['title'] = 't' * 101
        response = self.client.post('/alVatross/post/insert', self.params)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'タイトルの文字数が100文字を超えています')

    ########################################
    # test post edit.
    ########################################
    def test_initialize_post_edit(self):
        response = self.client.get('/alVatross/post/' + str(self.post.id))
        self.assertEqual(response.status_code, 200)

    def test_post_edit_404(self):
        response = self.client.get('/alVatross/post/missing_post_id')
        self.assertEqual(response.status_code, 404)

    ########################################
    # test post delete.
    ########################################
    def test_initialize_post_delete(self):
        response = self.client.get('/alVatross/post/delete/' + str(self.post.id))
        self.assertEqual(response.status_code, 302)

    def test_post_delete_404(self):
        response = self.client.get('/alVatross/post/delete/missing_post_id')
        self.assertEqual(response.status_code, 404)


class IndexBeforePostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'test_user'
        )
        self.client = Client()
        self.post = Post.objects.create(
            title = 'test post',
            content = 'test content',
            status = 'active',
            user_id = self.user.id
        )

    def test_post_list_before_login(self):
        response = self.client.get('/alVatross/post/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/alVatross/login?next=/alVatross/post/')

    def test_post_insert_before_login(self):
        response = self.client.get('/alVatross/post/insert')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/alVatross/login?next=/alVatross/post/insert')

    def test_post_edit_before_login(self):
        response = self.client.get('/alVatross/post/' + str(self.post.id))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/alVatross/login?next=/alVatross/post/' + str(self.post.id))

    def test_post_delete_before_login(self):
        response = self.client.get('/alVatross/post/delete/' + str(self.post.id))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/alVatross/login?next=/alVatross/post/delete/' + str(self.post.id))


