from django import forms
from django.forms import inlineformset_factory


from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', ]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'name', 'pages', 'price']

BookFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=2)