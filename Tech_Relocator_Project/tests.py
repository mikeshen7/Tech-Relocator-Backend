from django.test import TestCase
from django.contrib.auth import get_user_model

class UserProfileTests(TestCase):
    def test_token_view(self):
        data = {
            'username': 'admin',
            'password': '1234',
        }
        response = self.client.post("https://tech-relocator-backend.vercel.app/api/token/", data=data)
        self.assertEqual(response.status_code, 200)

        access_token = response.json().get('access')
        self.assertIsNotNone(access_token)

        # Test Refresh
        refresh_token = response.json().get('refresh')
        data = {
            'refresh': refresh_token,
        }
        refresh_response = self.client.post("https://tech-relocator-backend.vercel.app/api/token/refresh/", data=data)
        new_access_token = response.json().get('access')
        self.assertIsNotNone(new_access_token)

    def test_bad_login_view(self):
        data = {
            'username': 'admin',
            'password': '1',
        }
        response = self.client.post("https://tech-relocator-backend.vercel.app/api/token/", data=data)
        self.assertEqual(response.status_code, 401)
