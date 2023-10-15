class NumberValidate:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, name):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.isvalid(value):
            instance.__dict__[self.name] = value
    
    @classmethod
    def isvalid(self, value):
        return isinstance( value, (int, float) )
    

class Line:
    x1 = NumberValidate()
    x2 = NumberValidate()
    y1 = NumberValidate()
    y2 = NumberValidate()

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def __len__(self):
        length = ( (self.x2 - self.x1)**2 + (self.y2 - self.y1)**2 )**0.5
        if length < 1:
            return 0
        
        return length

