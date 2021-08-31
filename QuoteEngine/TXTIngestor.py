"""Extract data from TXT file."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
  """Class for parsing TXT files."""

  allowed_extensions = ['txt']

  @classmethod
  def parse(cls, path: str) -> List[QuoteModel]:
    """Parse method.
    
    param path: path to docx file.
    """
    if not cls.can_ingest(path):
      raise Exception("cannot ingest exception")
    
    quotes = []

    with open(path, 'r') as file:
      content = file.read()
      lines = content.split('\n')

      for line in lines:
        if line != "" and line != '\x0c':
          parsed = line.split('-')
          for num, elem in enumerate(parsed):
            parsed[num] = elem.strip()
          new_quote = QuoteModel(parsed[1], parsed[0])
          quotes.append(new_quote)

    return quotes