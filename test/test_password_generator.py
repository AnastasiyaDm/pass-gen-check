from unittest import TestCase
import password_generator
import string


class TestPasswordGenerator(TestCase):
    def test_generate_password(self):
        password_valid = password_generator.generate_password()
        self.assertTrue(any(symbol.isdigit() for symbol in password_valid))
        self.assertTrue(any(symbol.islower() for symbol in password_valid))
        self.assertTrue(any(symbol.isupper() for symbol in password_valid))
        self.assertTrue(any(symbol in string.punctuation for symbol in password_valid))
        self.assertGreaterEqual(len(password_valid), 14)
