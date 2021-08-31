"""An abstract base class for ingestor type classes."""

from typing import List
from abc import ABC, abstractmethod

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
  """IngestorInterface class."""

  allowed_extensions = []

  @classmethod
  def can_ingest(cls, path: str) -> bool:
    """Check ingest extension."""
    ext = path.split('.')[-1]
    return ext in cls.allowed_extensions

  @classmethod
  @abstractmethod
  def parse(cls, path: str) -> List[QuoteModel]:
    """Parse method."""
    pass