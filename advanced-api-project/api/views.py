from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ------------------------------
# LIST + CREATE VIEW
# ------------------------------
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books
    POST: Create a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]



class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single book
    PUT/PATCH: Update a book (authenticated users only)
    DELETE: Delete a book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
