"""Interface for data ingestion."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Interface which provide necessary method and abstract method for data ingestion."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Class method for validate support file format.
        
        param path: file path
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract parse method for parsing file and extract needed information and return the contents.
        
        param path: file path
        """
        pass
