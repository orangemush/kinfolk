import json
import bcrypt
from unittest.mock import patch, MagicMock

from django.test   import TestCase, Client

from user.models   import Account

class AccountSignUpTest(TestCase):
    def setUp(self):
        Account.objects.create(
            email    = 'testuser@gmail.com',
            password = bcrypt.hashpw("abcdefgh".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )

    def tearDown(self):
        Account.objects.all().delete

    def test_sign_up_success(self):
        client  = Client()
        account = {
            "email"   : "orangemusha@gmail.com",
            "password": "abcdefgh"
        }
        response = client.post('/user/sign_up', json.dumps(account), content_type = 'application/json')

        self.assertEqual(response.status_code, 200)

    def test_sign_up_duplicated_account(self):
        client  = Client()
        account = {
            "email"    : "testuser@gmail.com",
            "password" : "abcdefgh"
        }
        response = client.post('/user/sign_up', json.dumps(account), content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message': 'DUPLICATED_USER'
            }
        )
    
    def test_sign_up_invalid_keys(self):
        client  = Client()
        account = {
            "aaa"      : "orangemushab@gmail.com",
            "password" : "abcdefgh"
        }
        response = client.post('/user/sign_up', json.dumps(account), content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
            'message': 'KEY_ERROR'
            }
        )

class AccountLogInTest(TestCase):
    def setUp(self):
        Account.objects.create(
            email    = 'testuser@gmail.com',
            password = bcrypt.hashpw(
                    'abcdefgh'.encode('utf-8'),
                    bcrypt.gensalt()).decode('utf-8')
        )
    
    def tearDown(self):
        Account.objects.get(email = 'testuser@gmail.com').delete()

    def test_login_success(self):
        client  = Client()
        account = {
            "email"    : "testuser@gmail.com",
            "password" : "abcdefgh"
        }
        response = client.post('/user/login', json.dumps(account), content_type = 'application/json')

        self.assertEqual(response.status_code, 200)
    
    def test_login_not_exist_account(self):
        client  = Client()
        account = {
            "email"    : "notExisT@acd.com",
            "password" : "abcdefgh"
        }
        response = client.post('/user/login', json.dumps(account), content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message': 'INVALID_USER'
            }
        )

    def test_login_invalid_keys(self):
        client = Client()
        account = {
            "el"    : "orangemusha@gmail.com",
            "password" : "abcdefgh"
        }
        response = client.post('/user/login', json.dumps(account), content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message': 'KEY_ERROR'
            }
        )