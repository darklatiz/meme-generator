"""Module to contain all the Quote engine classes."""
from abc import ABC, abstractmethod
from subprocess import Popen, PIPE, check_output
from typing import List
import docx
import csv
import shlex


class QuoteModel:
    """Class representing a Quote."""

    def __init__(self, author, body):
        """Create a simple Quote Model containing the author and the body of the Quote."""
        self.__author = author
        self.__body = body

    @property
    def quote(self):
        """Create a property to access quotes' body value."""
        return self.__body

    @property
    def author(self):
        """Create a property to access quotes' author."""
        return self.__author

    @quote.setter
    def quote(self, new_quote):
        """Set new value to quotes' body."""
        self.__body = new_quote

    def __str__(self):
        """Create a readable representation of the Quote."""
        return f"I am A Quote: {self.author} said '{self.quote}'"


class IngestorInterface(ABC):
    """Base/Parent class to create a family os strategies for parsing different kind of files."""

    allowed_extensions = []

    @classmethod
    def set_allowed_extensions(cls, allowed):
        """Initialize text extensions."""
        cls.allowed_extensions = allowed

    @classmethod
    def clean(cls, word: str):
        """Clean remove characters."""
        w = word.strip().replace("'", "").replace('"', "")
        return w

    @classmethod
    def tokenize_quote(cls, word: str, splitter_character: str):
        """Split the word using the splitter character."""
        if splitter_character not in word:
            return None, None
        parts = word.split(splitter_character)
        quote_body = cls.clean(parts[0])
        quote_author = cls.clean(parts[1])
        return quote_author, quote_body

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the ingestor is able to parse a file."""
        if path is None or len(path) <= 0 or '.' not in path:
            raise Exception("Path is not valid")
        index = -1
        while path[index] != '.':
            index -= 1

        ext = path[index + 1:]

        if ext not in cls.allowed_extensions:
            return False
        return True

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file."""
        pass


class TXTIngestor(IngestorInterface):
    """Text Ingestor."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a TEXT file and create a list of Quote Models."""
        if cls.can_ingest(path):
            quotes = list()
            with open(path, 'r') as in_file:
                for line in in_file:
                    # line = "line" - author and To be or not to be - Perrofono
                    author, body = cls.tokenize_quote(line, '-')
                    if author is not None and body is not None:
                        quotes.append(QuoteModel(author, body))

            return quotes
        else:
            raise Exception(f"File {path} cannot be parsed")

    def __str__(self):
        """Found String representation of the object."""
        return f"I am a TXTIngestor, extensions_allowed = {self.allowed_extensions}"


class CSVIngestor(IngestorInterface):
    """CSV Ingestor."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a CSV File and create a list of Quote Models."""
        if cls.can_ingest(path):
            quotes = list()
            with open(path, 'r') as file_csv:
                reader = csv.DictReader(file_csv)
                for row in reader:
                    if row['author'] is not None and row['body'] is not None:
                        quotes.append(QuoteModel(row['author'], row['body']))
                return quotes
        else:
            raise Exception(f"File {path} cannot be parsed")

    def __str__(self):
        """Create String representation of the Object."""
        return f"I am a CSVIngestor, extensions allowed = {self.allowed_extensions}"


class PDFIngestor(IngestorInterface):
    """PDF Ingestor."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a PDF File and create a list of Quote Models."""
        if cls.can_ingest(path):
            quotes = list()
            command = ['pdftotext', '-layout', path, '-']
            output = check_output(command).decode()
            lines = output.split("\n")
            for line in lines:
                author, body = cls.tokenize_quote(line, '-')
                if author is not None and body is not None:
                    quotes.append(QuoteModel(author, body))
            return quotes
        else:
            raise Exception(f"File {path} cannot be parsed")

    def __str__(self):
        """Create String representation of the Object."""
        return f"I am a PDFIngestor, extensions allowed = {self.allowed_extensions}"


class DOCXIngestor(IngestorInterface):
    """DOCx Ingestor."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a Doc File and create a list of Quote Models."""
        if cls.can_ingest(path):
            doc = docx.Document(path)
            quotes = list()
            for p in doc.paragraphs:
                author, body = cls.tokenize_quote(p.text, '-')
                if author is not None and body is not None:
                    quotes.append(QuoteModel(author, body))
            return quotes
        else:
            raise Exception(f"File {path} cannot be parsed")

    def __str__(self):
        """Create String representation of the object."""


class Ingestor(IngestorInterface):
    """Ingestor will return the proper Ingestor available."""

    __ingestors = []

    def __init__(self):
        txt_ = TXTIngestor()
        txt_.set_allowed_extensions(['txt', 'text'])

        csv_ = CSVIngestor()
        csv_.set_allowed_extensions(['csv'])

        pdf_ = PDFIngestor()
        pdf_.set_allowed_extensions(['pdf'])

        docx_ = DOCXIngestor()
        docx_.set_allowed_extensions(['docx'])
        self.__ingestors.append(txt_)
        self.__ingestors.append(csv_)
        self.__ingestors.append(pdf_)
        self.__ingestors.append(docx_)

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the proper ingestor, if available, to parse given path file."""
        for ingestor in cls.__ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

