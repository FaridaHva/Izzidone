from django.test import TestCase

from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'pass12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.asserEqual(user.email, email)
        self.asserTrue(user.check_password(password))
