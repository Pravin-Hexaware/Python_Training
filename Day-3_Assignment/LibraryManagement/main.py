
from book import Book
from member import Member

book1=Book("Python Basics","Alice","ISBN0001")
book2=Book("Learning OOP","Bob","ISNN000")
book3=Book("Java Basics","John","ISBN003")


for b in [book1,book2,book3]:
    b.display()

m1=Member("Alice",101)
m2=Member("Bob",102)

m1.borrow_book(book1)
m1.borrow_book(book2)
m1.borrow_book(book3)
m2.borrow_book(book1)

m1.display_books()
m2.display_books()

m1.return_books(book2)
m2.borrow_book(book2)

