"""Read CSV file and extract body and author content from each line."""

from QuoteEngine.QuoteModel import QuoteModel
import csv
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class for validate extension and a parse CSV file."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method for parsing csv and extract needed information and return the contents.
        
        param path: csv file path
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest csv')

        quotes = []
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for r in reader:
                quotes.append(QuoteModel(r['body'], r['author']))

        return quotes
