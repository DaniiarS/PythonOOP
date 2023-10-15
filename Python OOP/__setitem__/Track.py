class Track:

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.route = []
    
    def add_point( self, x, y , speed ):
        self.route.append((x, y, speed))
    
    def __getitem__(self, item):
        if not isinstance(item, int) or (item < 0 or item > len(self.route)):
            raise IndexError('некорректный индекс')

        return (self.route[item][0], self.route[item][1]), self.route[item][2]
    
    def __setitem__(self, key, value):
        if not isinstance( key, int ) or ( key < 0 or key > len(self.route) ):
            raise IndexError('некорректный индекс')
        if not isinstance( value, (float, int) ):
            raise TypeError
        if value < 0:
            raise ValueError
        
        self.route[key] = (self.route[key][0], self.route[key][1], value)
        
        return self

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
coord, speed = tr[0]
tr[0] = 90
print( tr[0] )