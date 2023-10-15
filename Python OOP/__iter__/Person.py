class StringValidate:
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, name):
        return instance.__dict___[self.name]
    
    def __set__(self, instance, value):
        if not self.validate(value):
            raise ValueError
        
        instance.__dict__[self.name] = value
        return self

    def validate(self, value):
        return isinstance( value, str )

class IntValidate:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, name):
        return instance.__dict___[self.name]
    
    def __set__(self, instance, value):
        if not self.validate(value):
            raise ValueError
        
        instance.__dict__[self.name] = value
        return self

    def validate(self, value):
        return isinstance( value, int )

class FloatValidate:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, name):
        return instance.__dict___[self.name]
    
    def __set__(self, instance, value):
        if not self.validate(value):
            raise ValueError
        
        instance.__dict__[self.name] = value
        return self

    def validate(self, value):
        return isinstance( value, (float, int) )

class Person:

    fio = StringValidate()
    job = StringValidate()
    old = IntValidate()
    salary = FloatValidate()
    year_job = IntValidate()

    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.count = 0
    
    def __getitem__(self, index):
        attributes = list(self.__dict__.keys())
        if not (isinstance(index, int) or ( index < 0 or index >= len(attributes) - 1)):
            raise IndexError('неверный индекс')

        return self.__dict__[attributes[index]]
    
    def __setitem__(self, index, value):
        attributes = list(self.__dict__.keys())
        if not (isinstance(index, int) or ( index < 0 or index >= len(attributes) - 1)):
            raise IndexError('неверный индекс')
        
        self.__dict__[attributes[index]] = value
        return self

    def __iter__(self):
        return self
    
    def __next__(self):
        attributes = list(self.__dict__.keys())
        if self.count < len(attributes) - 1:
            res = self.__getitem__(self.count)
            self.count += 1
            return res
        else:
            self.count = 0
            raise StopIteration
            

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)