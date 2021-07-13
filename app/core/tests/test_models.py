from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        test_email = "asdf@asdf.ru"
        test_password = "Pass123"

        user = get_user_model().objects.create_user(
            email=test_email,
            password=test_password
        )

        self.assertEqual(user.email, test_email)
        self.assertTrue(user.check_password(test_password))

    def test_user_email_normalize(self):
        test_email = "asdf@ASDF.RU"

        user = get_user_model().objects.create_user(
            email=test_email,
            password="Pass123"
        )

        self.assertEqual(user.email, test_email.lower())

    def test_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', "123")

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email="asdf@asdf.df",
            password="qwe123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

