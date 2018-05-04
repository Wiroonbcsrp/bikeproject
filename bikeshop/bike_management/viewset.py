from rest_framework import viewsets
from .serializer import Bookserializer, Categoryserializer
from .models import Book


# ViewSets define the view behavior.
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

