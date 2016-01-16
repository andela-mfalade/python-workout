    import mock
    import unittest


class WhatIsGoingOnHere(unittest.TestCase):
    def setUp(self):
        self.new_instance = Object()
        self.new_instance.call_test_method = MagicMock(
            return_value="test@email.com")

    def test_returns_correct_email_addy(self):
        self.assertEquals(
            self.new_instance.call_test_method(),
            "test@email.com"
        )

