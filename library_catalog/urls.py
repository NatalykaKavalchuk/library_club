from django.urls import path
import library_catalog.views

app_name = 'library_catalog'

urlpatterns = [
    path('', library_catalog.views.home_page, name='home_page'),
    path('test/', library_catalog.views.test, name='test'),
    path('search/', library_catalog.views.search, name='search'),

    # ___BOOK___
    path('books/', library_catalog.views.list_books, name='books'),
    path('books/<slug:slug>', library_catalog.views.book_details, name='book_details'),
    path('books/add/book', library_catalog.views.add_book, name='add_book'),
    path('books/delete/<slug:slug>', library_catalog.views.delete_book, name='delete_book'),
    path('books/<slug:slug>/add_author', library_catalog.views.add_author_to_book, name='new_author'),

    # ___AUTHOR___
    path('authors/', library_catalog.views.list_authors, name='authors'),
    path('authors/<slug:slug>', library_catalog.views.author_details, name='author_details'),
    path('authors/add/author', library_catalog.views.add_author, name='add_author'),


]
