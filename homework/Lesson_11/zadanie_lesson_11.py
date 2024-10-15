# Библиотека
# Первый класс
# Создайте класс book с атрибутами:
#
# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
#
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
#
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
#
# Второй класс
#
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
#
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9

class Book:
    def __init__(self, title, author, pages, material, text, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.material = material
        self.has_text = text
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        text_est = "текст" if self.has_text else ""
        reservation = "зарезервирована" if self.reserved else ""
        return f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, " \
               f"материал: {self.material}, {text_est}" + (", " + reservation if reservation else "")


book1 = Book("Идиот", "Достоевский", 100, "бумага", True, "123-459-789", reserved=True)
book2 = Book("Book2", "Author2", 200, "бумага", True, "123-456-789")
book3 = Book("Book3", "Author3", 300, "картон", True, "123-456-789")
book4 = Book("Book4", "Author4", 400, "бумага", True, "123-456-789", reserved=True)
book5 = Book("Book5", "Author5", 500, "бумага", True, "123-456-789")

books = [book1, book2, book3, book4, book5]

# pro knigu:
for book in books:
    print(book)

print("________________")


class BooksForScool(Book):
    def __init__(self, title, author, pages, material, text, isbn, subject, school_year, exercises,
                 reserved=False):
        super().__init__(title, author, pages, material, text, isbn, reserved)
        self.exercises = exercises
        self.subject = subject
        self.school_year = school_year

    def __str__(self):
        reservation = "зарезервирована" if self.reserved else ""
        exercises = "с заданиями" if self.exercises else "без заданий"
        return f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, " \
               f"класс: {self.school_year}, {exercises}" + (", " + reservation if reservation else "")


school_book1 = BooksForScool("Алгебра", "Иванов", 200, "бумага", True, "123-456-789", "математика", 9, True,
                             reserved=True)
school_book2 = BooksForScool("school_book2", "Author2", 180, "paper", True, "123-456-789", "история", 8, False)
school_book3 = BooksForScool("school_book3", "Author3", 150, "paper", True, "123-456-789", "география", 7, True)
school_book4 = BooksForScool("English", "Author4", 220, "paper", True, "123-456-789", "english", 10, False,
                             reserved=True)

books_for_scool = [school_book1, school_book2, school_book3, school_book4]

for book in books_for_scool:
    print(book)
