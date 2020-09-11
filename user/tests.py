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

class KakaoLogInTest(TestCase):
    def setUp(self):
        Account.objects.create(
            email    = 'feisyhe@naver.com',
            kakao_id = "1471204013"
        ).save()

    def tearDown(self):
        Account.objects.get(email = 'feisyhe@naver.com').delete()

    @patch("user.views.requests")
    def test_kakao_login_success(self, mocked_request):
        class MockedResponse:
            def json(self):
                user_info = {
                    "id": "1471204013",
                    "kakao_account": {
                        "email": 'feisyhe@naver.com'
                    }
                }
                return user_info

        mocked_request.get = MagicMock(return_value = MockedResponse())
        client             = Client()
        response           = client.get("/user/kakao_login", content_type = "applications/json")
        
        self.assertEqual(response.status_code, 200)
    

    @patch("user.views.requests")
    def test_kakao_login_not_found(self, mocked_request):
        class MockedResponse:
            def json(self):
                user_info = {
                    "id": "1471204013",
                    "kakao_account": {
                        "email": 'feisyhe@naver.com'
                    }
                }
                return user_info

        mocked_request.get = MagicMock(return_value = MockedResponse())
        client             = Client()
        response           = client.get("/user/not_found", content_type = "applications/json")
        
        self.assertEqual(response.status_code, 404)

    @patch("user.views.requests")
    def test_kakao_login_key_error(self, mocked_request):
        class MockedResponse:
            def json(self):
                user_info = {
                    "id": None,
                    "kakao_account": {
                        "email": 'feisyhe@naver.com'
                    }
                }
                return user_info

        mocked_request.get = MagicMock(return_value = MockedResponse())
        client             = Client()
        response           = client.get("/user/kakao_login", content_type = "applications/json")
        
        self.assertEqual(response.status_code, 400)
