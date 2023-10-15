class Cell:

    def __init__(self, value):
        self.value = value
    

class SparseTable:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.content = {}
    
    def add_data(self, row, col, data):
        self.content[ (row, col) ] = data
        self.rows = max([ pair[0] for pair in self.content.keys() ]) + 1
        self.cols = max([ pair[1] for pair in self.content.keys() ]) + 1
        return self

    def remove_data(self, row, col):
        if (row, col) not in self.content.keys():
            raise IndexError('ячейка с указанными индексами не существует')

        del self.content[(row, col)]
        self.rows = max([ pair[0] for pair in self.content.keys() ]) + 1
        self.cols = max([ pair[1] for pair in self.content.keys() ]) + 1
    
    def __getitem__(self, pair):
        if ( pair[0], pair[1] ) not in self.content.keys():
            raise ValueError('данные по указанным индексам отсутствуют')

        return self.content[ (pair[0], pair[1]) ].value
    
    def __setitem__(self, pair, value):
        if  (pair[0], pair[1]) not in self.content.keys():
            self.add_data( pair[0], pair[1], Cell(value) )
            return self
        
        self.content[ (pair[0], pair[1]) ].value = value
        return self



st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError

