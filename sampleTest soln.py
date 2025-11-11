import math

class Author:
    def __init__(self, author_name, birthdate):
        self.author_name = author_name
        self.birthdate = birthdate
        
    def __str__(self):
        return f"Author: {self.author_name.upper()}, Birthdate: {self.birthdate}"
    

class Content:
    def __init__(self, title, page_num, price):
        self.title = title
        self.page_num = page_num
        self.price = price

    def __str__(self):
        return f"Content: {self.title.upper()}, Pages: {self.page_num}, Price: {self.price}"


class Book(Author, Content):
    def __init__(self, title, author_name, birthdate, page_num, price):
        Author.__init__(self, author_name, birthdate)
        Content.__init__(self, title, page_num, price)
      
    def __str__(self):
        return (
            f"BOOK(TITLE: {self.title.upper()}, "
            f"AUTHOR: {self.author_name.upper()}, "
            f"BIRTHDATE: {self.birthdate}, "
            f"PAGES: {self.page_num}, "
            f"PRICE: {self.price})"
        )

    def calculate_book_value(self):
        return math.sqrt((self.price ** 2) * self.page_num)
    
    # comparison operators (we’ll implement in Exercise 2)
    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

# test it
book1 = Book("The Concept", "Ms Cynthia", "1990-01-01", 200, 30.0)
book2 = Author("Mr John", "1985-05-15")
bookcontent = Content("Learning Python", 350, 45.0)
print(bookcontent)
