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

class DataBase:

    def __init__(self, path):
        self.path = path
        self.dict_db = {}
    
    def write(self, record):
        if record in self.dict_db.keys():
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = [record]
    
    def read(self, pk):
        for key in self.dict_db.keys():
            for value in self.dict_db[key]:
                if value.pk == pk:
                    return value  

class Record:
    pk = 0

    fio = StringValidate()
    descr = StringValidate()
    old = IntValidate()

    def __init__(self, fio, descr, old ):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.increase_pk()
        
    @classmethod
    def increase_pk(cls):
        cls.pk += 1
        return cls.pk

    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __hash__(self):
        return hash((self.fio.lower(), self.old))
    
db = DataBase("path")
lst_in = list(map(str.strip, sys.stdin.readlines()))

for entry in lst_in:
    name, occup, age = entry.split(';')
    db.write(Record(name, occup, int(age)))
d = tuple(db.dict_db.values())
# print(db.read(1))

# for entry in db.dict_db.keys():
#     print( entry.pk, entry.fio, entry.descr, entry.old )

# print( db.read(5) )
# print( db.dict_db )
