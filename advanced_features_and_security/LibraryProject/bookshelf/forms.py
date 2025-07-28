from django import forms
from .models import Book  # Or replace `Book` with your actual model if different

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Replace with the correct model if not Book
        fields = ['title', 'author', 'description']  # Use actual model fields
