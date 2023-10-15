class NumberValidate:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, name):
        if self.name not in instance.__dict__:
            return None

        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.isvalid(value):
            instance.__dict__[self.name] = value
    
    @classmethod
    def isvalid(cls, value):
        return isinstance( value, (int, float) )

class Ellipse:
    x1 = NumberValidate()
    y1 = NumberValidate()
    x2 = NumberValidate()
    y2 = NumberValidate()

    def __init__(self, *args, **kwargs):
        if len(args) == 4:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]
    
    def __bool__(self):
        return len(self.__dict__) == 4
    
    def get_coords(self):
        if len(self.__dict__) != 4:
            raise AttributeError('нет координат для извлечения')

        return (self.x1, self.y1, self.x2, self.y2)

st_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]

for ellipse in st_geom:
    if ellipse:
        ellipse.get_coords()

