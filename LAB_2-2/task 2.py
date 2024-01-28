class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


book = Book(id_=1, name='test_name_1', pages=200)
print(book)
print(repr(book))


class Library:
    def __init__(self, books=[]):
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            last_book = self.books[-1]
            return last_book.id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


library = Library()
print(library.get_next_book_id())