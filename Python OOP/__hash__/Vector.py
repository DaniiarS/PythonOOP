class Vector:
    
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and type(args[0]) is list:
            self.vector = args[0]

        lst = []
        for element in args:
            if not isinstance(element, (float, int)):
                raise TypeError
            lst.append(element)
        self.vector = lst
    


    def __add__(self, other):
        if len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')

        lst = []
        for i in range(len(self)):
            lst.append(self.vector[i] + other.vector[i])
        
        return Vector(lst)
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')

        lst = []
        for i in range(len(self)):
            lst.append(self.vector[i] - other.vector[i])
        
        return Vector(lst)

    def __mul__(self, other):
        if len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')

        lst = []
        for i in range(len(self)):
            lst.append(self.vector[i] * other.vector[i])
        
        return Vector(lst)
    
    def __iadd__(self, other):
        if isinstance(other, (float, int)):
            for i in range(len(self.vector)):
                self.vector[i] += 10
            return self
        elif isinstance(other, Vector):
            return self + other
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __isub__(self, other):
        if isinstance(other, (float, int)):
            for i in range(len(self.vector)):
                self.vector[i] -= 10
            return self
        elif isinstance(other, Vector):
            return self - other
        else:
            raise ArithmeticError('размерности векторов не совпадают')
    
    def __eq__(self, other):
        if len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')

        for i in range(len(self.vector)):
            if self.vector[i] != other.vector[i]:
                return False
        return True

    def __len__(self):
        return len(self.vector)



