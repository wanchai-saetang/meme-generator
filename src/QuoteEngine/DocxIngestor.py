"""Read Docx file and extract body and author content from each line."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Class for validate extension and a parse Docx file."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method for parsing docx and extract needed information and return the contents.
        
        param path: docx file path
        """
        if not cls.can_ingest(path):
            raise Exception("cannot ingest docx")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split("-")
                body = parse[0].strip('" ')
                author = parse[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
