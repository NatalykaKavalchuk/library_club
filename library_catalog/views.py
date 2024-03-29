from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from library_catalog.forms import BookForm, AuthorForm
from library_catalog.models import Book, Author


def home_page(request):
    return render(request, 'home_page.html')


def test(request):
    return render(request, 'test.html')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        search_obj = Book.objects.filter(title__icontains=searched)
        search_author = Author.objects.filter(Q(first_name__icontains=searched) | Q(last_name__icontains=searched))

        return render(request, 'search_authors.html',
                      {'searched': searched, 'search_obj': search_obj, 'search_author': search_author})
    else:
        return render(request, 'search_authors.html')


# ___BOOK___

def list_books(request):
    all_books = Book.objects.all()
    paginator = Paginator(all_books, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'all_books.html', {'all_books': page_obj})


def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    assoc_authors = book.author.all()
    non_assoc_authors = Author.objects.exclude(books=book)
    data = {
        "book": book,
        "assoc_authors": assoc_authors,
        "non_assoc_authors": non_assoc_authors
    }
    return render(request, 'book_details.html', data)


def delete_book(request, slug):
    book = Book.objects.get(slug=slug)
    book.delete()
    return redirect('library_catalog:books')


def add_author_to_book(request, slug):
    if request.POST['author_slug']:
        book = Book.objects.get(slug=slug)
        new_author = Author.objects.get(slug=request.POST['author_slug'])
        book.author.add(new_author)

    return redirect('library_catalog:books')


def add_book(request):
    if request.method == "POST":
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():

            book_form.save()
            messages.success(request, 'Your book was successfully added!')
            return redirect('library_catalog:books')
        else:
            messages.error(request, 'Error saving form')

    book_form = BookForm()
    all_books = Book.objects.all()
    return render(request, 'add_book.html', context={'book_form': book_form, 'all_books': all_books})


# ___AUTHOR___

def list_authors(request):
    all_authors = Author.objects.all()

    paginator = Paginator(all_authors, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'all_authors.html', {'all_authors': page_obj})


def author_details(request, slug):
    author = Author.objects.get(slug=slug)

    return render(request, 'author_details.html', {'author': author})


def add_author(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST, request.FILES)
        if author_form.is_valid():

            author_form.save()
            messages.success(request, 'Author was successfully added!')
            return redirect('library_catalog:authors')
        else:
            messages.error(request, 'Error saving form')

    author_form = AuthorForm()
    all_authors = Author.objects.all()
    return render(request, 'add_author.html', context={'author_form': author_form, 'all_authors': all_authors})
