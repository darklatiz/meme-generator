"""Module to test the Quote Engine."""

import unittest
import pathlib

from src.QuoteEngine.Quote import TXTIngestor, CSVIngestor, PDFIngestor, DOCXIngestor, QuoteModel

TESTS_ROOT = (pathlib.Path(__file__).parent).resolve()
TEST_TXT_FILES = [TESTS_ROOT / 'test-dog-quotes.txt', TESTS_ROOT / 'test-simple-lines.text']
TEST_CSV_FILES = [TESTS_ROOT / 'test-dog-quotes.csv', TESTS_ROOT / 'test-simple-lines.csv']
TEST_PDF_FILES = [TESTS_ROOT / 'test-dog-quotes.pdf', TESTS_ROOT / 'test-simple-lines.pdf']
TEST_DOCX_FILES = [TESTS_ROOT / 'test-dog-quotes.docx', TESTS_ROOT / 'test-simple-lines.docx']


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
            self.assertTrue(txt_ingestor.can_ingest(str(path_file)))

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

    def test_txt_ingestor_parse(self):
        txt_ingestor = TXTIngestor()
        txt_ingestor.set_allowed_extensions(['text', 'txt'])

        for text_file in TEST_TXT_FILES:
            quotes_lst = txt_ingestor.parse(str(text_file))
            self.assertIsNotNone(quotes_lst)
            self.assertTrue(len(quotes_lst) > 0)
            for q in quotes_lst:
                self.assertIsInstance(q, QuoteModel)
                print(q)

    def test_txt_ingestor_parse_exception(self):
        txt_ingestor = TXTIngestor()
        txt_ingestor.set_allowed_extensions(['text', 'txt'])

        with self.assertRaises(Exception):
            txt_ingestor.parse('')

        with self.assertRaises(Exception):
            txt_ingestor.parse('some')

    def test_csv_ingestor_can_ingest_allowed_extensions(self):
        csv_ingestor = CSVIngestor()
        csv_ingestor.set_allowed_extensions(['csv'])
        self.assertIsNotNone(csv_ingestor)
        for path_file in TEST_CSV_FILES:
            self.assertTrue(csv_ingestor.can_ingest(str(path_file)))

    def test_csv_ingestor_cannot_ingest_not_allowed_extensions(self):
        csv_ingestor = TXTIngestor()
        csv_ingestor.set_allowed_extensions(['csv'])
        self.assertIsNotNone(csv_ingestor)
        self.assertFalse(csv_ingestor.can_ingest('some_file.texto'))
        self.assertFalse(csv_ingestor.can_ingest('some_file.tst'))
        self.assertFalse(csv_ingestor.can_ingest('some_file.pdf'))

    def test_csv_ingestor_raise_exceptions(self):
        csv_ingestor = TXTIngestor()
        csv_ingestor.set_allowed_extensions(['csv'])
        with self.assertRaises(Exception):
            csv_ingestor.can_ingest('')

        with self.assertRaises(Exception):
            csv_ingestor.can_ingest('file-without_extension')

    def test_csv_ingestor_parse(self):
        csv_ingestor = CSVIngestor()
        csv_ingestor.set_allowed_extensions(['csv'])

        for text_file in TEST_CSV_FILES:
            quotes_lst = csv_ingestor.parse(str(text_file))
            self.assertIsNotNone(quotes_lst)
            self.assertTrue(len(quotes_lst) > 0)
            for q in quotes_lst:
                self.assertIsInstance(q, QuoteModel)
                print(q)

    def test_csv_ingestor_parse_exception(self):
        csv_ingestor = CSVIngestor()
        csv_ingestor.set_allowed_extensions(['csv'])

        with self.assertRaises(Exception):
            csv_ingestor.parse('')

        with self.assertRaises(Exception):
            csv_ingestor.parse('some')

    def test_pdf_ingestor_can_ingest_allowed_extensions(self):
        pdf_ingestor = PDFIngestor()
        pdf_ingestor.set_allowed_extensions(['pdf'])
        self.assertIsNotNone(pdf_ingestor)
        for path_file in TEST_PDF_FILES:
            self.assertTrue(pdf_ingestor.can_ingest(str(path_file)))

    def test_pdf_ingestor_cannot_ingest_not_allowed_extensions(self):
        pdf_ingestor = PDFIngestor()
        pdf_ingestor.set_allowed_extensions(['pdf'])
        self.assertIsNotNone(pdf_ingestor)
        self.assertFalse(pdf_ingestor.can_ingest('some_file.texto'))
        self.assertFalse(pdf_ingestor.can_ingest('some_file.tst'))
        self.assertFalse(pdf_ingestor.can_ingest('some_file.dox'))

    def test_pdf_ingestor_raise_exceptions(self):
        pdf_ingestor = PDFIngestor()
        pdf_ingestor.set_allowed_extensions(['pdf'])
        with self.assertRaises(Exception):
            pdf_ingestor.can_ingest('')

        with self.assertRaises(Exception):
            pdf_ingestor.can_ingest('file-without_extension')

    def test_docx_ingestor_can_ingest_allowed_extensions(self):
        docx_ingestor = DOCXIngestor()
        docx_ingestor.set_allowed_extensions(['docx', 'doc'])
        self.assertIsNotNone(docx_ingestor)
        for path_file in TEST_DOCX_FILES:
            self.assertTrue(docx_ingestor.can_ingest(str(path_file)))

    def test_docx_ingestor_cannot_ingest_not_allowed_extensions(self):
        docx_ingestor = DOCXIngestor()
        docx_ingestor.set_allowed_extensions(['docx', 'doc'])
        self.assertIsNotNone(docx_ingestor)
        self.assertFalse(docx_ingestor.can_ingest('some_file.texto'))
        self.assertFalse(docx_ingestor.can_ingest('some_file.tst'))
        self.assertFalse(docx_ingestor.can_ingest('some_file.dox'))

    def test_docx_ingestor_raise_exceptions(self):
        docx_ingestor = DOCXIngestor()
        docx_ingestor.set_allowed_extensions(['docx', 'doc'])
        with self.assertRaises(Exception):
            docx_ingestor.can_ingest('')

        with self.assertRaises(Exception):
            docx_ingestor.can_ingest('file-without_extension')
