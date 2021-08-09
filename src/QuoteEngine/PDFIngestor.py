"""Read Docx file and extract body and author content from each line."""

from typing import List

from QuoteEngine.QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .TXTIngestor import TXTIngestor

import pathlib
import random
import subprocess
import os


class PDFIngestor(IngestorInterface):
    """Class for validate extension and a parse PDF file."""

    allowed_extensions = ["pdf"]

    pdf_tools = pathlib.Path("./pdftotext")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method for call pdf_tools to convert pdf to text before read and return content from text file.
        
        param path: pdf file path
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest pdf')

        pathlib.Path('./tmp').mkdir(exist_ok=True)

        tmp = pathlib.Path(f"./tmp/{random.randint(0,1000000)}.txt")
        subprocess.call([cls.pdf_tools.resolve(), path, tmp])

        tmp_text_path = str(tmp.resolve())
        txt_content = TXTIngestor.parse(tmp_text_path)
        os.remove(tmp_text_path)
        return txt_content
