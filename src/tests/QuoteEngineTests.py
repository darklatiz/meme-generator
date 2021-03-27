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

    def test_txt_ingestor_can_ingest_allowed_extensions(self):
        txt_ingestor = TXTIngestor()
        txt_ingestor.set_allowed_extensions(['text', 'txt'])
        self.assertIsNotNone(txt_ingestor)
        for path_file in TEST_TXT_FILES:
            self.assertTrue(txt_ingestor.can_ingest(path_file.name))

    def test_txt_ingestor_cannot_ingest_not_allowed_extensions(self):
        txt_ingestor = TXTIngestor()
        txt_ingestor.set_allowed_extensions(['text', 'txt'])
        self.assertIsNotNone(txt_ingestor)
        self.assertFalse(txt_ingestor.can_ingest('some_file.texto'))
        self.assertFalse(txt_ingestor.can_ingest('some_file.tst'))
        self.assertFalse(txt_ingestor.can_ingest('some_file.pdf'))

    def test_txt_ingestor_raise_exceptions(self):
        txt_ingestor = TXTIngestor()
        txt_ingestor.set_allowed_extensions(['text', 'txt'])
        with self.assertRaises(Exception):
            txt_ingestor.can_ingest('')

        with self.assertRaises(Exception):
            txt_ingestor.can_ingest('file-without_extension')

