from django.db import models
from django.utils import timezone

class Author(models.Model):
    """
    Author model stores basic information about book authors.
    One author can have multiple books (One-to-Many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an Author.
    It includes a ForeignKey to Author to establish the relationship.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
