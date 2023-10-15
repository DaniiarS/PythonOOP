import sys

class StringValidate:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, name):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.isvalid(value):
            instance.__dict__[self.name] = value
    
    @classmethod
    def isvalid(self, value):
        return type(value) is str

class MailItem:
    
    mail_from = StringValidate()
    title = StringValidate()
    content = StringValidate()

    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False
    
    def set_read(self, fl_read):
        self.is_read = fl_read
    
    def __bool__(self):
        return self.is_read

class MailBox:
    
    def __init__(self, lst = []):
        self.inbox_list = lst
    
    def receive(self):
        lst_in = list(map( str.strip, sys.stdin.readlines() ))
        self.inbox_list = [ MailItem( mail.split('; ')[0], mail.split('; ')[1], mail.split('; ')[2]) for mail in lst_in ]

mail = MailBox()
mail.receive()

mail.inbox_list[0].set_read(True)
mail.inbox_list[1].set_read(True)

inbox_list_filtered = list(filter(bool, mail.inbox_list))
