"""Extract data from CSV file."""

import pandas
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
  """Class for parsing CSV files."""

  allowed_extensions = ['csv']

  @classmethod
  def parse(cls, path: str) -> List[QuoteModel]:
    """Parse method.
    
    param path: path to csv file.
    """
    if not cls.can_ingest(path):
      raise Exception("cannot ingest exception")
    
    quotes = []
    df = pandas.read_csv(path, header=0)

    for index, row in df.iterrows():
      new_quote = QuoteModel(row['author'], row['body'])
      quotes.append(new_quote)
    
    return quotes