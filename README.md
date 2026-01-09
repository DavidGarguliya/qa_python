# qa_python

## Тесты BooksCollector
- `test_add_new_book_add_two_books` пример: добавление двух книг и проверка количества.
- `test_add_new_book_invalid_title_not_added` параметризация: пустое имя и имя >40 символов не сохраняются.
- `test_set_book_genre_handles_valid_and_invalid` параметризация: жанр записывается только из допустимого списка, иначе остается пустым.
- `test_get_book_genre_returns_none_for_unknown` запрос жанра несуществующей книги возвращает `None`.
- `test_get_books_with_specific_genre_filters_correctly` возвращает только книги выбранного жанра.
- `test_get_books_genre_returns_mapping` выдаёт актуальный словарь книг и их жанров (у новых книг жанр пустой).
- `test_get_books_for_children_excludes_age_rating` исключает жанры с возрастным рейтингом из детского списка.
- `test_add_book_in_favorites_only_existing_and_unique` добавляет в избранное только существующую книгу и без дублей.
- `test_delete_book_from_favorites_removes_book` удаляет книгу из избранного и оставляет список актуальным.

## Запуск
```bash
pytest -v tests.py
```
