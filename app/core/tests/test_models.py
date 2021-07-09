from django.test import TestCase
from django.contrib.auth import get_user_model, models


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        test_email = "asdf@asdf.ru"
        test_password = "Pass123"

        user: models.User = get_user_model().objects.create_user(
            email=test_email,
            password=test_password
        )

        self.assertEqual(user.email, test_email)
        self.assertTrue(user.check_password(test_password))
