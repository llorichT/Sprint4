from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')

        assert '1984' in collector.get_books_genre()

    def test_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', [
        '',
        'a' * 41
    ])
    def test_add_book_invalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_set_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Роман')

        assert collector.get_book_genre('1984') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        result = collector.get_books_with_specific_genre('Фантастика')

        assert '1984' in result

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        result = collector.get_books_for_children()

        assert '1984' in result
        assert 'Оно' not in result

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')

        assert '1984' in collector.get_list_of_favorites_books()

    def test_add_nonexistent_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('1984')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')

        assert '1984' not in collector.get_list_of_favorites_books()
