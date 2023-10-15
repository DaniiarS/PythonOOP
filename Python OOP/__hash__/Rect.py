class ValidateNumber:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.isvalid(value):
            instance.__dict__[self.name] = value
        else:
            raise TypeError(f"{self.name} must be of type int or float")
    
    @classmethod
    def isvalid(cls, value):
        return isinstance(value, (int, float))

class Rect:
    
    x = ValidateNumber()
    y = ValidateNumber()
    width = ValidateNumber()
    height = ValidateNumber()
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash((self.height,self.width))

r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2


print(h1, h2)
