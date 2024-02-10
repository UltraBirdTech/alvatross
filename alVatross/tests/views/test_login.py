from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'test_user',
            password = 'password'
        )
        self.client = Client()
        self.params = {
            'loginid': self.user.username,
            'password': self.user.password
        }

    # ====================================================
    # login() test
    # ====================================================
    def test_initialize(self):
        response = self.client.get('/alVatross/login')
        self.assertEqual(response.status_code, 200)

    def test_success_login(self):
        response = self.client.post('/alVatross/login', self.params)
        self.assertEqual(response.status_code, 302)

    def test_success_login_as_hash(self):
        user = User.objects.create(
            username = 'test_user_password_hash',
            password = make_password('password')
        )
        params = {
            'loginid': user.username,
            'password': 'password' 
        }
        response = self.client.post('/alVatross/login', params)
        self.assertEqual(response.status_code, 302)

    def test_invalid_login_username_failed(self):
        self.params['loginid'] = 'invalid username'
        response = self.client.post('/alVatross/login', self.params)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '指定されたユーザが存在しません。')

    def test_invalid_login_password_failed(self):
        self.params['password'] = 'invalid password'
        response = self.client.post('/alVatross/login', self.params)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'パスワードが間違っています。')

    # ====================================================
    # loout() test
    # ====================================================
    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get('/alVatross/logout')
        self.assertEqual(response.status_code, 302)

    # ====================================================
    # forget_password() test
    # ====================================================
    def test_forget_password(self):
        response = self.client.get('/alVatross/forget_password/')
        self.assertEqual(response.status_code, 200)

    def test_forget_password_post(self):
        params = {
            'loginid': self.user.username
        }
        response = self.client.post('/alVatross/forget_password/', params)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.password)

    def test_forget_password_invalid_username(self):
        params = {
            'loginid': 'invalid username'
        }
        response = self.client.post('/alVatross/forget_password/', params)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '指定されたユーザが存在しません。')

class BeforeLoginTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_initialize_before_login(self):
        response = self.client.get('/alVatross/login')
        self.assertEqual(response.status_code, 200)
