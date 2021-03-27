"""Module to test the Quote Engine."""

import unittest
import pathlib

from src.QuoteEngine.Quote import TXTIngestor

TESTS_ROOT = (pathlib.Path(__file__).parent).resolve()
TEST_TXT_FILES = [TESTS_ROOT / 'test-dog-quotes.txt', TESTS_ROOT / 'test-simple-lines.text']


class QuoteEngineTest(unittest.TestCase):

    @classmethod
    def set_up(cls):
        """Set up the env for the test cases."""
        pass

    def test_txt_ingestor(self):
        txt_ingestor = TXTIngestor(['txt', 'text'])
        self.assertIsNotNone(txt_ingestor)
