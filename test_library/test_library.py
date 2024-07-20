import unittest
from main import Library


class TestLibraryMethods(unittest.TestCase):

    def setUp(self):
        self.library = Library('test_library_data.json')
        self.library.add_book('Тестовая книга 1', 'Тестовый автор 1', '2022')
        self.library.add_book('Тестовая книга 2', 'Тестовый автор 2', '2021')

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 2)
        self.library.add_book('Тестовая книга 3', 'Тестовый автор 3', '2020')
        self.assertEqual(len(self.library.books), 3)

    def test_delete_book(self):
        self.library.delete_book(1)
        self.assertEqual(len(self.library.books), 1)
        self.library.delete_book(2)
        self.assertEqual(len(self.library.books), 0)

    def test_search_book(self):
        result = self.library.search_book('title', 'Тестовая книга 1')
        self.assertEqual(result[0].title, 'Тестовая книга 1')

        result = self.library.search_book('author', 'Тестовый автор 2')
        self.assertEqual(result[0].author, 'Тестовый автор 2')

    def test_change_status(self):
        self.library.change_status(1, 'выдана')
        self.assertEqual(self.library.books[0].status, 'выдана')

    def tearDown(self):
        with open('test_library_data.json', 'w') as file:
            file.write('[]')


if __name__ == '__main__':
    unittest.main()
