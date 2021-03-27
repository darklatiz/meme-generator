"""Module to contain all the Quote engine classes."""
from abc import ABC, abstractmethod
from typing import List


class QuoteModel:
    """Class representing a Quote."""

    def __init__(self, author, body):
        """Create a simple Quote Model containing the author and the body of the Quote."""
        self.author = author
        self.body = body

    def __str__(self):
        """Create a readable representation of the Quote."""
        return f"I am A Quote: {self.author} said '{self.body}'"


class IngestorInterface(ABC):
    """Base/Parent class to create a family os strategies for parsing different kind of files."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the ingestor is able to parse a file"""

        if path is None or len(path) <= 0:
            raise Exception("Path is not valid")

        parts = path.split('.')
        return parts[-1] in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file"""
        pass


class TXTIngestor(IngestorInterface):
    """Text Ingestor"""

    def __init__(self, allowed_extensions):
        """Initialize text extensions"""
        self.allowed_extensions = allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

    def __str__(self):
        """String representation of the object."""
        return f"I am a TXTIngestor, extensions_allowed = {self.allowed_extensions}"
