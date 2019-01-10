from django import forms
from .models import Book

class TestForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_code','book_title', 'author_name', 'publisher', 'category')
