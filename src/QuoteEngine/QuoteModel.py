"""Represent models for Quote.

The `QuteModel` class represents a Quote object. Each has a quote body and author.
"""

class QuoteModel:
    """Represent models for Quote."""

    def __init__(self, body, author):
        """Create Quote Model object to store quote body and author information.
        
        param body: quote body
        param author: quote author
        """
        self.body = body
        self.author = author

    def __str__(self) -> str:
        """Beautify print object."""
        return f"{self.body}({self.author})"

    def __repr__(self) -> str:
        """Beautify represent object."""
        return f"{self.body}({self.author})"
