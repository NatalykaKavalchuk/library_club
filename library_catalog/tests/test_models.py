from django.test import TestCase
from django.utils.text import slugify

from library_catalog.models import Author


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Natallia', last_name='Kavalchuk')

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

    def test_author_slug(self):
        author = Author.objects.create(first_name='Big', last_name='Bob')

        self.assertEqual(author.slug, slugify(f'{author.first_name} {author.last_name}'))


