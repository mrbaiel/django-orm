from django.template.defaultfilters import first
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .models import Catalog


from .views import home

class URLsTest(SimpleTestCase):
    """ тестируем URLs"""

    def test_homepage_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)


class CatalogModelTests(TestCase):
    """ Тест каталога модели """

    def setUp(self):
        self.book = Catalog(
            title="Django Book",
            ISBN='123-4352-12',
            author='Sartbaev Baiel',
            price='123.99',
            availibility=True,
        )

    def test_create_book(self):
        self.assertIsInstance(self.book, Catalog)

    def test_book_names(self):
        self.assertEqual(str(self.book), 'Django Book')

    def test_saving_and_retrieving_book(self):
        first_book = Catalog()
        first_book.title = "Django Book"
        first_book.ISBN = "123-4352-12"
        first_book.author = "Sartbaev Baiel"
        first_book.price = "123.99"
        first_book.availibility = 'True'
        first_book.save()

        second_book = Catalog()
        second_book.title = "Second Django Book"
        second_book.ISBN = "231-3214-23"
        second_book.author = "Bekmurzaev Jamo"
        second_book.price = "321.99"
        second_book.availibility = 'False'
        second_book.save()

        saved_books = Catalog.objects.all()
        self.assertEqual(saved_books.count(), 2)

        first_saved_book = saved_books[0]
        second_saved_book = saved_books[1]
        self.assertEqual(first_saved_book.title, 'Django Book')
        self.assertEqual(second_saved_book.author, 'Bekmurzaev Jamo')
