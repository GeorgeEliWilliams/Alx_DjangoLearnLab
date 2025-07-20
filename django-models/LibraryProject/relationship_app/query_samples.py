from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by", author_name + ":", books_by_author)

# Query 2: List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in", library_name + ":", books_in_library)

# Query 3: Retrieve the librarian for a library
librarian = library.librarian
print("Librarian of", library_name + ":", librarian.name)
