#this one works after Brendan fixed it but his does not. 
from Author import Author
from Book import Book


a1 = Author("Bob", "BobNickName")

b1 = Book("Pet Cemetery", a1)

b1.author.printpen()

