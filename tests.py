import unittest
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library()
        self.library.books = []

    def test_add_book(self) -> None:
        self.library.add_book("Test Book", "Author", "2020")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_remove_book(self) -> None:
        self.library.add_book("Test Book", "Author", "2020")
        book_id = self.library.books[0].id
        self.library.remove_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_update_status(self) -> None:
        self.library.add_book("Test Book", "Author", "2020")
        book_id = self.library.books[0].id
        self.library.update_status(book_id)
        self.assertEqual(self.library.books[0].status, "выдана")


if __name__ == "__main__":
    unittest.main()
