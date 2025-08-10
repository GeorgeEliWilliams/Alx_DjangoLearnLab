from django.shortcuts import render
from rest_framework import generics, permissions
from django.views.generic import ListView, DetailView, UpdateView, DeleteView  
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books
    POST: Create a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single book
    PUT/PATCH: Update a book (authenticated users only)
    DELETE: Delete a book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'  


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_form.html'


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/'
    template_name = 'book_confirm_delete.html'
