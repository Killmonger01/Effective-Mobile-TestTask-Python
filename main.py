from library import Library


def main() -> None:
    """
    Основная программа для управления библиотекой.
    """
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            library.add_book(title, author, year)
        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            library.remove_book(book_id)
        elif choice == "3":
            search_term = input("Введите название, автора или год издания книги: ")
            library.search_books(search_term)
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            book_id = input("Введите ID книги: ")
            library.update_status(book_id)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
