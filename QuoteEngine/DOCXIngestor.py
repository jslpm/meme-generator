"""Extract data from DOCX file."""

import docx
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DOCXIngestor(IngestorInterface):
  """Class for parsing DOCX files."""

  allowed_extensions = ['docx']

  @classmethod
  def parse(cls, path: str) -> List[QuoteModel]:
    """Parse method.
    
    param path: path to docx file.
    """
    if not cls.can_ingest(path):
      raise Exception("cannot ingest exception")

    quotes = []
    doc = docx.Document(path)

    for paragraph in doc.paragraphs:
      if paragraph.text != "":
        parsed = paragraph.text.split('-')
        new_quote = QuoteModel(parsed[1], parsed[0])
        quotes.append(new_quote)
    
    return quotes