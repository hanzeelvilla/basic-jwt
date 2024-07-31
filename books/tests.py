from django.test import TestCase

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        cls.book = Book.objects.create(
            title = "Naruto",
        )
    
    def test_book_model(self):
        self.assertEqual(self.book.title, "Naruto")
        self.assertEqual(str(self.book), "Naruto")