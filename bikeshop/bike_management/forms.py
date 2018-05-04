from django.forms import ModelForm
from .models import Book, Category


class addBook(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'publish_date', 'category', 'detail', 'images']
