# Створення класу Book для представлення книги
class Book:
    # Ініціалізація екземпляра класу з заданими параметрами
    def __init__(self, price, numberOfPages, author, quantity, numberOfSales):
        # Ініціалізація властивостей книги
        self.price = price
        self.numberOfPages = numberOfPages
        self.author = author
        self.quantity = quantity
        self.numberOfSales = numberOfSales

    # Визначення методу __str__ для форматованого представлення об'єкта книги
    def __str__(self):
        return f"{self.author}: {self.numberOfPages} pages, Price: {self.price}, Available: {self.quantity}, Sold: {self.numberOfSales}"

    # Метод для редагування властивостей книги
    def edit_book(self, price=None, numberOfPages=None, author=None, quantity=None, numberOfSales=None):
        # Зміна властивостей книги, якщо вони надані
        if price is not None:
            self.price = price
        if numberOfPages is not None:
            self.numberOfPages = numberOfPages
        if author is not None:
            self.author = author
        if quantity is not None:
            self.quantity = quantity
        if numberOfSales is not None:
            self.numberOfSales = numberOfSales

# Створення класу BookShop для управління магазином книг
class BookShop:
    # Ініціалізація магазину
    def __init__(self):
        self.books = []  # Список книг у магазині

    # Метод для додавання книги до магазину
    def add_book(self, book):
        self.books.append(book)

    # Метод для видалення книги з магазину
    def remove_book(self, book):
        self.books.remove(book)

    # Метод для редагування книги в магазині
    def edit_book(self, book, **kwargs):
        book.edit_book(**kwargs)

    # Метод для пошуку книги за автором
    def find_book_by_author(self, author):
        return next((book for book in self.books if book.author == author), None)

    # Метод для сортування книг за заданим критерієм
    def sort_books(self, by='price'):
        return sorted(self.books, key=lambda x: getattr(x, by), reverse=True)

    # Метод для відображення всіх книг у магазині
    def display_books(self):
        for book in self.books:
            print(book)

# Головне меню для управління книжковим магазином
def main_menu():
    shop = BookShop()  # Створення екземпляра магазину
    while True:
        # Виведення меню
        print("\nBook Shop Management")
        print("1. Add a new book")
        print("2. Edit a book")
        print("3. Remove a book")
        print("4. Display books")
        print("5. Sort books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # Обробка вибору користувача
        if choice == '1':
            # Логіка для додавання нової книги
            price = int(input("Enter book price: "))
            numberOfPages = int(input("Enter number of pages: "))
            author = input("Enter author's name: ")
            quantity = int(input("Enter quantity: "))
            numberOfSales = int(input("Enter number of sales: "))
            book = Book(price, numberOfPages, author, quantity, numberOfSales)
            shop.add_book(book)
        elif choice == '2':
            # Логіка для редагування книги
            author = input("Enter the author of the book to edit: ")
            book = shop.find_book_by_author(author)
            if book:
                price = input("Enter new price (press enter to skip): ")
                numberOfPages = input("Enter new number of pages (press enter to skip): ")
                quantity = input("Enter new quantity (press enter to skip): ")
                numberOfSales = input("Enter new number of sales (press enter to skip): ")
                kwargs = {
                    "price": int(price) if price else None,
                    "numberOfPages": int(numberOfPages) if numberOfPages else None,
                    "quantity": int(quantity) if quantity else None,
                    "numberOfSales": int(numberOfSales) if numberOfSales else None
                }
                shop.edit_book(book, **kwargs)
            else:
                print("Book not found.")
        elif choice == '3':
            # Логіка для видалення книги
            author = input("Enter the author of the book to remove: ")
            book = shop.find_book_by_author(author)
            if book:
                shop.remove_book(book)
            else:
                print("Book not found.")
        elif choice == '4':
            # Відображення всіх книг у магазині
            shop.display_books()
        elif choice == '5':
            # Сортування книг за заданим критерієм
            criteria = input("Enter sort criteria (price/numberOfSales): ")
            sorted_books = shop.sort_books(by=criteria)
            for book in sorted_books:
                print(book)

        elif choice == '6':
            break  # Вихід з програми
        else:
            print("Invalid choice. Please try again.")

# Запуск головного меню, якщо скрипт виконується як головний
if __name__ == "__main__":
    main_menu()
