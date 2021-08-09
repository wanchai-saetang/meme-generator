"""Wrapper for data ingestion support multiple extensions."""

from typing import List

from .IngestorInterface import IngestorInterface
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Class for validate extension and a parse multiple format file."""

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method for parsing multiple format file and extract needed information and return the contents.
        
        param path: file path which support various format
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
