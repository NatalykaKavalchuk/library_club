from django.test import TestCase


class HomePageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class BooksPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get("/books/")
        self.assertTemplateUsed(response, "all_books.html")


class AuthorsPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/authors/")
        self.assertEqual(response.status_code, 200)
