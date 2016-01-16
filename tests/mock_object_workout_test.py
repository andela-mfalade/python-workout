import unittest

from mock import MagicMock

from scripts import nigeria_states


class TestNigeriaStates(unittest.TestCase):
    def setUp(self):
        self.country = nigeria_states.Nigeria()
        self.country.retrieve_current_country_president = MagicMock(
            return_value="General Buhari")

    def test_returns_correct_country_president(self):
        presido = self.country.retrieve_current_country_president
        self.assertEquals(
            presido(),
            "General Buhari"
        )
