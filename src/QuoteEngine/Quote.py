"""Module to contain all the Quote engine classes."""
from abc import ABC, abstractmethod
from typing import List
import csv


class QuoteModel:
    """Class representing a Quote."""

    def __init__(self, author, body):
        """Create a simple Quote Model containing the author and the body of the Quote."""
        self.__author = author
        self.__body = body

    @property
    def quote(self):
        """Create a property to access quotes' body value"""
        return self.__body

    @property
    def author(self):
        return self.__author

    @quote.setter
    def quote(self, new_quote):
        """Set new value to quotes' body"""
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
        """Clean remove characters"""
        w = word.strip().replace("'", "").replace('"', "")
        return w

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
                    parts = line.split('-')
                    quote_body = cls.clean(parts[0])
                    quote_author = cls.clean(parts[1])
                    quotes.append(QuoteModel(quote_author, quote_body))

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

    def __str__(self):
        """Create String representation of the Object."""
        return f"I am a PDFIngestor, extensions allowed = {self.allowed_extensions}"


class DOCXIngestor(IngestorInterface):
    """DOCx Ingestor."""

    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a Doc File and create a list of Quote Models."""

    def __str__(self):
        """Create String representation of the object."""
