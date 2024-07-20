import json
from typing import List, Union

class Book:
    """класса Book, который инициализирует атрибуты экземпляра книги"""
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


class Library:
    """класса Library, инициализирует атрибуты экземпляра библиотеки"""
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.books = self.load_data()

    def load_data(self) -> List[Book]:
        """Метод для загрузки данных о книгах из файла JSON.
        Если файл не найден или данные некорректны, возвращает пустой список"""
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                return [Book(book['id'], book['title'], book['author'], book['year'], book['status']) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self) -> None:
        """Метод для сохранения данных о книгах в файл JSON"""
        data = [{'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year, 'status': book.status}
                for book in self.books]
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Метод для добавления новой книги в библиотеку с указанным названием, автором и годом.
         Сохраняет данные в файл"""
        new_id = len(self.books) + 1
        new_book = Book(new_id, title, author, year, 'в наличии')
        self.books.append(new_book)
        self.save_data()

    def delete_book(self, book_id: int) -> None:
        """Метод для удаления книги по её ID.
        Если книга с таким ID не найдена, выводит сообщение об ошибке"""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_data()
                return
        print('Книга с указанным ID не найдена')

    def search_book(self, key: str, value: str) -> Union[List[Book], str]:
        """Метод для поиска книг по заданному ключу и значению"""
        result = [book for book in self.books if value.lower() in str(getattr(book, key)).lower()]
        if result:
            return result
        else:
            return 'Книги не найдены'

    def display_all_books(self) -> None:
        """Метод для отображения информации о всех книгах в библиотеке"""
        for book in self.books:
            print(
                f'ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}')

    def change_status(self, book_id: int, new_status: str) -> None:
        """Метод для изменения статуса книги по её ID.
        Если книга с таким ID не найдена, выводит сообщение об ошибке"""
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_data()
                return
        print('Книга с указанным ID не найдена')

