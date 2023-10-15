class ValidateNumber:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.isvalid(value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")

    @classmethod
    def isvalid(cls, value):
        return value >= 0 and (type(value) is int or type(value) is float)

class Dimensions:

    a = ValidateNumber()
    b = ValidateNumber()
    c = ValidateNumber()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __hash__(self):
        return hash( (self.a, self.b, self.c ) )

lst = input().split(';')
lst_dims = [ Dimensions( x.split()[0],  x.split()[1],  x.split()[2] ) for x in lst ]

lst_dims = sorted( lst_dims, key = lambda x: hash(x) )
print(lst_dims)