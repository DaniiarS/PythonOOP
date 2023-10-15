class Integer:
    
    def __init__(self, start_value = 0):
        if not isinstance(start_value, int):
            raise ValueError('должно быть целое число')
        
        self.start_value = start_value
    
    @property
    def value(self):
        return self.start_value
    
    @value.setter
    def value(self, value):
        if not isinstance( value, int ):
            raise ValueError('должно быть целое число')

        self.start_value = value

class Array:

    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.array = [0 for i in range(max_length)]

    def __getitem__(self, item):
        if not isinstance( item ,int ) or ( item < 0 or item >= self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

        return self.array[item]
    
    def __setitem__(self, key, value):
        if not isinstance( key, int ) or ( key < 0 or key >= self.max_length ):
            raise IndexError('неверный индекс для доступа к элементам массива')

        if not isinstance( value, int ):
            raise ValueError
        
        self.array[key] = value
        return self
    

    def __str__(self):
        res = ""
        for i in range(self.max_length):
            if( i == self.max_length - 1):
                res += str(self.array[i])
                break;
            
            res += str(self.array[i]) + " "
        
        return res

a = Array(2, Integer)
a[0] = 1
a[1] = 2
print( str(a) )