"""Read text file and extract body and author content from each line."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Class for validate extension and a parse text file."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method for parsing text and extract needed information and return the contents.
        
        param path: docx file path
        """
        if not cls.can_ingest(path):
            raise Exception("cannot ingest txt")

        quotes = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    decode_line = line.strip('\n\r ')
                    split_line = decode_line.split("-")
                    body = split_line[0].strip()
                    author = split_line[1].strip()
                    quotes.append(QuoteModel(body, author))

        return quotes
