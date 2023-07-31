from django.test import TestCase
from model_bakery import baker

from library_catalog.models import Author, Book


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Natallia', last_name='Kavalchuk', slug="natallia_kavalchuk")

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.first_name} {author.last_name}'
        self.assertEquals(expected_object_name, str(author))



class BookModelTest(TestCase):
    # the test allows you to fill in the fields of the model 'Book' using the library model_bakery
    def test_book_model(self):
        book = baker.make(Book, title="I love Python")
        self.assertEqual(str(book), "I love Python")


class TestModels(TestCase):
    # testing two related models
    def test_book_has_an_author(self):
        book = Book.objects.create(title="I love Python")
        bob = Author.objects.create(first_name="Bob", last_name="Green", slug="bob-green")
        nick = Author.objects.create(first_name="Nick", last_name="Crain", slug="nick-crain")
        book.author.set([bob.pk, nick.pk])
        self.assertEqual(book.author.count(), 2)
