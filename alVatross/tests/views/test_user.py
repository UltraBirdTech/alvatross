from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User

class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'test user'
        )
        self.client = Client()
        self.client.force_login(self.user)

        self.params = {
            'username': 'test create user',
            'email': 'test@example.jp',
            'password': 'testuser',
            'first_name': 'test',
            'last_name': 'user'
        }

    ########################################
    # test user list.
    ######################################## 
    def test_initialize(self):
        response = self.client.get('/alVatross/users/')
        self.assertEqual(response.status_code, 200)

    ########################################
    # test user isnert.
    ######################################## 
    
 
