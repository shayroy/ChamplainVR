import datetime

class Document:
    """This class defines documents."""
    def __init__(self, authors = []):
        #Constructor for documents.
        self.__authors = authors
        self.__date = datetime.datetime.now()

    def getAuthors(self):
        #Getter for authors.
        return self.__authors

    def addAuthor(self, name):
        #Method to add author.
        self.__authors.append(name)

    def getDate(self):
        #Getter for date.
        return self.__date

class Book:
    """This class defines books."""
    def __init__(self, title= ""):
        #Constructor for books
        self.__title = title

    def getTitle(self):
        #Getter for title.
        return self.__title

class Email:
    """This class defines emails."""
    def __init__(self, subject="", to=[]):
        #Constructor for emails.
        self.__subject = subject
        self.__to = to

    def getSubject(self):
        #Getter for subject.
        return self.__subject

    def getTo(self):
        #Getter for to.
        return self.__to

