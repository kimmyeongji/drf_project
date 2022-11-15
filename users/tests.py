from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User

# Create your tests here.
class UserRegistrationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            'username' : 'testuser',
            'fullname' : '테스트 유저',
            'email' : 'test@test.com',
            'password' : 'password',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 201) #201 CREATED

class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {'username':'test_user', 'password':'test'}
        self.user = User.objects.create_user('test_user', 'test')
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(response.status_code, 200)