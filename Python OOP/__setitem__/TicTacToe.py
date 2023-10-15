class Cell:
    
    def __init__(self, value = 0, is_free = True):
        self.value = value
        self.is_free = is_free 
    
    def __bool__(self):
        return self.is_free

class TicTacToe:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is not None:
            return cls.__instance
        return super().__new__(cls)
    
    def __init__(self):
        self.row = 3
        self.col = 3
        self.pole = [ [ Cell() for j in range( self.col )] for i in range( self.row ) ]

    def __getitem__(self, index):
        row, col = index[0], index[1]
        print( row, col )

        if not ( self.validateIndex(col) and self.validateIndex(row) ):
            raise IndexError('неверный индекс клетки')

        if not isinstance( row, int ):
            startR, stopR, stepR = self.normalizeSlice( row.start, row.stop, row.step )
            if not isinstance( col, int ):
                startC, stopC, stepC = self.normalizeSlice( col.start, col.stop, col.step )
                return tuple([ tuple([cell.value for cell in line]) for line in self.pole[ startR:stopR:stepR ][ startC:stopC:stepC ] ])
            return tuple(line[col].value for line in self.pole[ startR:stopR:stepR ])
        else:
            if not isinstance( col, int ):
                startC, stopC, stepC = self.normalizeSlice( col.start, col.stop, col.step )
                return tuple([ cell.value for cell in self.pole[row][startC:stopC:stepC] ])

        return self.pole[row][col].value

    def __setitem__(self, key, value):
        row, col = key[0], key[1]

        if not ( self.validateIndex(row) and self.validateIndex(col) ):
            raise IndexError('неверный индекс клетки')
        if not self.pole[row][col].is_free:
            raise ValueError('клетка уже занята')

        self.pole[row][col] = Cell(value, False)
        return self
    
    def show(self):
        for i in range(self.row):
            for j in range(self.col):
                print( self.pole[i][j].value, end = " ")
            print()
    
    def validateIndex(self, line):
        if not isinstance( line, (int, slice) ):
            return False
        return True
    
    def normalizeSlice(self, start, stop, step):
        if start is None:
            start = 0
        if stop is None:
            stop = self.row
        if step is None:
            step = 1
        return start, stop, step
    
    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0
        return self
    
    
g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"
try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"
    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3
assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"
cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"