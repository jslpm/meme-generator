"""Ingestor class.

Ingestor class encapsulates ingestor class for
CSV, PDF, DOCX and TXT extensions.
"""

from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.TXTIngestor import TXTIngestor
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor

class Ingestor(IngestorInterface):
  """Ingestor class."""

  ingestors = [DOCXIngestor, CSVIngestor, TXTIngestor, PDFIngestor]

  @classmethod
  def parse(cls, path: str) -> List[QuoteModel]:
    """Parse method in Ingestor class."""
    for ingestor in cls.ingestors:
      if ingestor.can_ingest(path):
        return ingestor.parse(path)