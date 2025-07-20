from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
orwell = Author.objects.get(name="George Orwell")
books_by_orwell = orwell.books.all()
print("Books by George Orwell:", books_by_orwell)

# Query 2: List all books in a library
central_library = Library.objects.get(name="Central Library")
books_in_library = central_library.books.all()
print("Books in Central Library:", books_in_library)

# Query 3: Retrieve the librarian for a library
librarian = central_library.librarian
print("Librarian of Central Library:", librarian.name)
t