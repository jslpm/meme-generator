"""QuoteModel class."""

class QuoteModel():
    """QuoteModel class."""
    
    def __init__(self, author=None, body=None):
        """Quote model constructor.
        
        param author: quotes's author
        param body: sentence
        """
        self.author = author
        self.body = body

    def __repr__(self) -> str:
        """Return repr(self), a readable string of the quote."""
        return f'{self.body} - {self.author}'