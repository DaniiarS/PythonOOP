from enum import unique
import sys

class StringValidate:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.isvalid(value):
            instance.__dict__[self.name] = value
    
    @classmethod
    def isvalid(cls, value):
        return type(value) is str

class IntValidate:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.isvalid(value):
            instance.__dict__[self.name] = value
    
    @classmethod
    def isvalid(cls, value):
        return type(value) is int

class BookStudy:

    name = StringValidate()
    author = StringValidate()
    year = IntValidate()
    
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    
    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = [ BookStudy(book.split(';')[0], book.split(';')[1], int(book.split(';')[2])) for book in lst_in ]

unique_books = len(set( lst_bs ))