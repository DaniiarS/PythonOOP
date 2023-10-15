class IntValidate:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, name):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.isvalid(value):
            if value <= 0:
                raise ValueError("длины сторон треугольника должны быть положительными числами")
            
            instance.__dict__[self.name] = value
    
    @classmethod
    def isvalid(self, value):
        return isinstance(value, (float, int))

class Triangle:
    
    a = IntValidate()
    b = IntValidate()
    c = IntValidate()
    
    def __init__(self, a, b, c):
        if ( a + b < c ) or ( a + c < b ) or ( b + c < a ):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

        self.a = a 
        self.b = b
        self.c = c

    def __len__(self):
        return int( self.a + self.b + self.c )
    
    def __call__(self):
        p = len(self)//2

        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5 






