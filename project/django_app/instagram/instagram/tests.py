from django.test import Client
from django.test import LiveServerTestCase

from member.models import User


class IndexTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_user_is_not_authenticaed_redirect_test_root_redirect_to(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/member/signup/')

    def test_user_is_authenticated_redirect_to_post_list(self):
        test_username = 'test_user'
        test_password = 'test_password'
        User.objects.create_user(test_username, test_password)
        self.client.post(
            '/member/login/',
            {
                'username': test_username,
                'password': test_password,
            }
        )
        response = self.client.get('/')
        self.assertRedirects(response, '/post/')

