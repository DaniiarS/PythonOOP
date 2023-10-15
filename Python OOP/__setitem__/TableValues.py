class IntegerValue:

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')

        instance.__dict__[self.name] = value
        

class CellInteger:

    value = IntegerValue()

    def __init__(self, start_value = 0):
        self.value = start_value
    
class TableValues:

    rows = IntegerValue
    cols = IntegerValue

    def __init__(self, rows, cols, cell = CellInteger):
        if cell is None:
            raise ValueError('параметр cell не указан')

        self.rows = rows
        self.cols = cols
        self.cells = tuple([ tuple([cell() for i in range(cols)]) for j in range(rows) ])
        self.objectType = cell
    
    def __getitem__(self, item):
        if not ( isinstance( item[0], int) and isinstance( item[1], int) ):
            raise TypeError

        if ( item[0] < 0 or item[0] > self.rows ) or ( item[1] < 0 or item[1] > self.cols ): 
            raise IndexError

        return self.cells[item[0]][item[1]].value  
    
    def __setitem__(self, key, value):
        if not( isinstance(key[0], int) and isinstance(key[1], int) ):
            raise KeyError
        
        if not isinstance( value, int ):
            raise ValueError
        
        if ( key[0] < 0 or key[0] >= self.rows ) or ( key[1] < 0 or key[1] >= self.cols ):
            raise IndexError
        
        tableRow = list( self.cells[key[0]])
        tableRow[key[1]] = self.objectType(value)
        
        table = list(self.cells)
        table[key[0]] = tuple(tableRow)
        self.cells = tuple( table )
        
        return self


table = TableValues(3, 2, cell=CellInteger)
table[0, 0] = 1
# table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()

print( table.cells )
    
    
