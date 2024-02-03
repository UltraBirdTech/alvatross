from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User

class IndexTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'test_user'
        )
        self.client = Client()
        self.client.force_login(self.user)

    def test_initialize(self):
        response = self.client.get('/alVatross/')
        self.assertEqual(response.status_code, 200)

class IndexBeforeLoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'test_user'
        )
        self.client = Client()

    def test_initialize_before_login(self):
        response = self.client.get('/alVatross/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/alVatross/login?next=/alVatross/')

