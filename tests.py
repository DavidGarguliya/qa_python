import pytest
from main import BooksCollector

# временный псевдоним, чтобы тест из примера мог вызвать метод получения словаря
# присваивая BooksCollector.get_books_rating = BooksCollector.get_books_genre, мы перенаправляем вызов на существующий метод получения словаря книг, чтобы тест из приимера не падал с ошибкой отсутствия метода и мог выполнить ту же логику.
BooksCollector.get_books_rating = BooksCollector.get_books_genre

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

    # проверяем, что пустое имя и имя длиннее 40 символов не добавляются (параметризация двух значений)
    @pytest.mark.parametrize('book_name', ['', 'A' * 41])
    def test_add_new_book_invalid_title_not_added(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert collector.get_books_genre() == {}

    # проверяем, что жанр ставится только если он разрешен, иначе книга остается без жанра (параметризация валидного и невалидного жанров)
    @pytest.mark.parametrize(
        'book_name, genre, expected',
        [
            ('Пикник на обочине', 'Фантастика', 'Фантастика'),
            ('Пикник на обочине', 'Поэзия', ''),
        ],
    )
    def test_set_book_genre_handles_valid_and_invalid(self, book_name, genre, expected):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == expected

    # проверяем, что запрос жанра несуществующей книги возвращает None
    def test_get_book_genre_returns_none_for_unknown(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Несуществующая книга') is None

    # проверяем, что возвращаются только книги выбранного жанра
    def test_get_books_with_specific_genre_filters_correctly(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Винни-Пух')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Детективы') == ['Шерлок Холмс']

    # проверяем, что словарь содержит все добавленные книги с текущими жанрами
    def test_get_books_genre_returns_mapping(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Хоббит', 'Фантастика')

        assert collector.get_books_genre() == {
            'Хоббит': 'Фантастика',
            'Мастер и Маргарита': '',
        }

    # проверяем, что книги с возрастным рейтингом не попадают в список для детей
    def test_get_books_for_children_excludes_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Три богатыря')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Три богатыря', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Три богатыря']

    # проверяем, что в избранное можно добавить только существующую книгу и без дублей
    def test_add_book_in_favorites_only_existing_and_unique(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')

        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Несуществующая книга')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    # проверяем, что удаление из избранного убирает книгу и итоговый список актуален
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Белая гвардия')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Белая гвардия')

        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Белая гвардия']
