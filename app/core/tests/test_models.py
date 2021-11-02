from django.test import TestCase
from django.contrib.auth import get_user_model

class TestsModel(TestCase):

    def test_create_user_with_email_successfull(self):
        # test create new user with email address
        email = 'email@london.com'
        password = 'test1234' 
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalize(self):
        # test the email for a new user is normalized
        email = 'test@LONDON.COM'
        user = get_user_model().objects.create_user(
            email,
            'fdjvfdnsb'
        )

        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        # test create user with no email raise error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test12345678')

    def test_create_new_super_user(self):
        # test create new super user
        user = get_user_model().objects.create_superuser(
            'test@abc.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)