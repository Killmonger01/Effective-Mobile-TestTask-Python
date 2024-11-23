import os
import json
from typing import Optional, List
from models import Book

DATA_FILE = os.path.join(os.getcwd(), "data", "library.json")


class Library:
    """
    Класс для управления библиотекой книг.
    """

    def __init__(self) -> None:
        self.books: List[Book] = []
        self.load_books()

    def load_books(self) -> None:
        """
        Загружает книги из файла JSON.
        """
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    self.books = [Book.from_dict(book) for book in data]
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Ошибка загрузки данных: {e}. Библиотека будет пуста.")
                self.books = []
        else:
            self.save_books()

    def save_books(self) -> None:
        """
        Сохраняет книги в файл JSON.
        """
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Добавляет книгу в библиотеку после проверки данных.
        """
        if not year.isdigit():
            print("Ошибка: год издания должен быть числом.")
            return
        book = Book(title=title, author=author, year=int(year))
        self.books.append(book)
        self.save_books()
        print(f"Книга '{title}' добавлена в библиотеку.")

    def remove_book(self, book_id: str) -> None:
        """
        Удаляет книгу по ID.
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"Книга '{book.title}' удалена из библиотеки.")
                return
        print("Ошибка: книга с таким ID не найдена.")

    def search_books(self, search_term: str) -> None:
        """
        Ищет книги по названию, автору или году.
        """
        results = [
            book for book in self.books
            if search_term.lower() in book.title.lower()
            or search_term.lower() in book.author.lower()
            or search_term == str(book.year)
        ]
        if results:
            print("Найденные книги:")
            for book in results:
                print(book)
        else:
            print("Книг по заданному запросу не найдено.")

    def display_books(self) -> None:
        """
        Выводит список всех книг.
        """
        if self.books:
            print("Список книг в библиотеке:")
            for book in self.books:
                print(book)
        else:
            print("Библиотека пуста.")

    def update_status(self, book_id: str) -> None:
        """
        Обновляет статус книги.
        """
        for book in self.books:
            if book.id == book_id:
                book.status = "выдана" if book.status == "в наличии" else "в наличии"
                self.save_books()
                print(f"Статус книги '{book.title}' обновлён на '{book.status}'.")
                return
        print("Ошибка: книга с таким ID не найдена.")
