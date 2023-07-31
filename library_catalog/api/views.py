from rest_framework import viewsets

from library_catalog.api.serializers import BookSerializer, AuthorSerializer
from library_catalog.models import Book, Author


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
