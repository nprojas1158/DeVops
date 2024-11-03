import unittest
from src.commands.authenticate import Authenticate
from src.errors.errors import MissingToken, Unauthorized

class TestAuthenticate(unittest.TestCase):
    def test_verify_valid_token(self):
        auth = Authenticate("Bearer 75c893b6-9084-4ce2-af52-805d5d124267")
        result = auth.verify()
        self.assertTrue(result)

    def test_verify_missing_token(self):
        auth = Authenticate(None)
        with self.assertRaises(MissingToken):
            auth.verify()

    def test_verify_invalid_token(self):
        auth = Authenticate("Bearer invalid-token")
        with self.assertRaises(Unauthorized):
            auth.verify()

    