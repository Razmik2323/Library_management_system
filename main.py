from library.library_functions import Library

def main():
    library = Library('library/library_data.json')

    while True:
        print('\n1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Найти книгу')
        print('4. Показать все книги')
        print('5. Изменить статус книги')
        print('6. Выйти')

        choice = input('Выберите действие: ')

        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            year = input('Введите год издания: ')
            library.add_book(title, author, year)

        elif choice == '2':
            book_id = int(input('Введите ID книги для удаления: '))
            library.delete_book(book_id)

        elif choice == '3':
            search_key = input('Выберите критерий поиска (title/author/year): ')
            search_value = input('Введите значение для поиска: ')
            results = library.search_book(search_key, search_value)
            if isinstance(results, list):
                for book in results:
                    print(
                        f'ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}')
            else:
                print(results)

        elif choice == '4':
            library.display_all_books()

        elif choice == '5':
            book_id = int(input('Введите ID книги для изменения статуса: '))
            new_status = input('Введите новый статус (в наличии/выдана): ')
            library.change_status(book_id, new_status)

        elif choice == '6':
            break

        else:
            print('Некорректный ввод. Попробуйте еще раз.')


if __name__ == "__main__":
    main()
