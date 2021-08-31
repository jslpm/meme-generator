"""Extract data from PDF file."""

import subprocess
import os
import random

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
  """Class for parsing PDF files."""
  
  allowed_extensions = ['pdf']

  @classmethod
  def parse(cls, path: str) -> List[QuoteModel]:
    """Parse method.
    
    param path: path to pdf file.
    """
    if not cls.can_ingest(path):
      raise Exception("cannot ingest exception")
    

    tmp = f"./{random.randint(0,10000000)}.txt"
    call = subprocess.call(['pdftotext', path, tmp])
    quotes = []
    
    with open(tmp, 'r') as file:
      content = file.read()
      lines = content.split('\n')

      for line in lines:
        if line != "" and line != '\x0c':
          parsed = line.split('-')
          for num, elem in enumerate(parsed):
            parsed[num] = elem.strip()
          new_quote = QuoteModel(parsed[1], parsed[0])
          quotes.append(new_quote)

    os.remove(tmp)

    return quotes