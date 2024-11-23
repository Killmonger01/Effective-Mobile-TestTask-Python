import uuid


class Book:
    """
    Класс для представления книги в библиотеке.
    """

    def __init__(self, title: str, author: str, year: int, book_id: str = None, status: str = "в наличии") -> None:
        self.id = book_id if book_id else str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """
        Преобразует объект книги в словарь.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """
        Создаёт объект книги из словаря.
        """
        return Book(
            title=data["title"],
            author=data["author"],
            year=int(data["year"]),
            book_id=data["id"],
            status=data["status"],
        )

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.
        """
        return f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"
