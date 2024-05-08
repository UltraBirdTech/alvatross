from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User

class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'test user',
            password = 'password'
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

    def test_initialize_user_type_admin(self):
        response = self.client.get('/alVatross/users/?user_type=Admin')
        self.assertEqual(response.status_code, 200)

    def test_initialize_user_type_user(self):
        response = self.client.get('/alVatross/users/?user_type=User')
        self.assertEqual(response.status_code, 200)

    ########################################
    # test user isnert.
    ######################################## 
    def test_initialize_user_insert(self):
        response = self.client.get('/alVatross/users/insert')
        self.assertEqual(response.status_code, 200)

    def test_user_insert(self):
        response = self.client.post('/alVatross/users/insert', self.params)
        self.assertEqual(response.status_code, 302)    

    def test_user_insert_duplicate_username(self):
        self.params['username'] = 'test user'
        response = self.client.post('/alVatross/users/insert', self.params)
        self.assertEqual(response.status_code, 200)    
        self.assertContains(response, '指定されたusernameは既に登録されています')

    # cut password 20 char.
    def test_user_insert_cut_password_19_char(self):
        self.params['password'] = 't' * 19
        response = self.client.post('/alVatross/users/insert', self.params)
        self.assertEqual(response.status_code, 302)    
        user = User.objects.get(username=self.params['username'])
        self.assertEqual(user.password, 't' * 19)

    def test_user_insert_cut_password_20_char(self):
        self.params['password'] = 't' * 20
        response = self.client.post('/alVatross/users/insert', self.params)
        self.assertEqual(response.status_code, 302)    
        user = User.objects.get(username=self.params['username'])
        self.assertEqual(user.password, 't' * 20)

    def test_user_insert_cut_password_21_char(self):
        self.params['password'] = 't' * 21
        response = self.client.post('/alVatross/users/insert', self.params)
        self.assertEqual(response.status_code, 302)    
        user = User.objects.get(username=self.params['username'])
        self.assertEqual(user.password, 't' * 20)


    ########################################
    # test user update.
    ######################################## 
    def test_initialize_user_edit(self):
        response = self.client.get('/alVatross/users/' + str(self.user.id))
        self.assertEqual(response.status_code, 200)

    def test_user_edit_404(self):
        response = self.client.get('/alVatross/users/missing_user_id')
        self.assertEqual(response.status_code, 404)

    def test_user_edit(self):
        response = self.client.post('/alVatross/users/' + str(self.user.id), self.params)
        self.assertEqual(response.status_code, 302) 

    def test_user_update_duplicate_username(self):
        self.params['username'] = 'test user'
        response = self.client.post('/alVatross/users/' + str(self.user.id), self.params)
        self.assertEqual(response.status_code, 200)    
        self.assertContains(response, '指定されたusernameは既に登録されています')

    # cut password 20 char.
    def test_user_update_cut_password_19_char(self):
        self.params['password'] = 't' * 19
        response = self.client.post('/alVatross/users/' + str(self.user.id), self.params)
        self.assertEqual(response.status_code, 302)    
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.password, 't' * 19)

    def test_user_update_cut_password_20_char(self):
        self.params['password'] = 't' * 20
        response = self.client.post('/alVatross/users/' + str(self.user.id), self.params)
        self.assertEqual(response.status_code, 302)    
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.password, 't' * 20)

    def test_user_update_cut_password_21_char(self):
        self.params['password'] = 't' * 21
        response = self.client.post('/alVatross/users/' + str(self.user.id), self.params)
        self.assertEqual(response.status_code, 302)    
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.password, 't' * 20)

    ########################################
    # test user delete.
    ########################################
    def test_user_delete(self):
        user = User.objects.create(
            username = 'test delete user'
        )
        response = self.client.get('/alVatross/users/delete/' + str(user.id))
        self.assertEqual(response.status_code, 302)

    def test_user_delete_invalid_self(self):
        response = self.client.get('/alVatross/users/delete/' + str(self.user.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '自分自身を削除することはできません')

    def test_user_delete_invalid_admin(self):
        user = User.objects.create(
            username = 'test delete admin user',
            is_superuser = True
        )
        response = self.client.get('/alVatross/users/delete/' + str(user.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '管理者権限ユーザは削除できません')

    def test_user_delete_404(self):
        response = self.client.get('/alVatross/users/delete/missing_post_id')
        self.assertEqual(response.status_code, 404)

