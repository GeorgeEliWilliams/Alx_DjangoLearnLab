from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# CSRF protection is automatically enabled for all views using Django templates.
# Still, we explicitly use csrf_protect for clarity and documentation.

@csrf_protect
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Use Django ORM to fetch all books safely (no risk of SQL injection)
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@csrf_protect
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Use Django forms for input validation (sanitizes input & protects against XSS/SQL injection)
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Safe ORM save
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

@csrf_protect
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # Safe object retrieval, returns 404 if not found
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'form': form})

@csrf_protect
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})
