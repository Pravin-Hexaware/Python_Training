class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.__availability=True

    def is_available(self):
        return self.__availability
    
    def borrow(self):
        if self.__availability:
            self.__availability=False
            return True
        return False
    
    def return_book(self):
        self.__availability=True

    def display(self):
        status="Available" if self.__availability else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author},ISBN: {self.isbn}, Status: {status}")

        