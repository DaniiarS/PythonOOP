class RadiusVector:

    def __init__(self, *args, **kwargs):
        self.coords = []
        for element in args:
            if not isinstance( element, (int, float) ):
                raise TypeError
            self.coords.append( element )
    
    def __getitem__(self, item):
        if not isinstance( item, (int, slice) ):
            raise IndexError
        if isinstance( item , int) and ( item < 0 or item >= len(self.coords)):
            raise IndexError

        if isinstance(item, slice):
            start, stop, step = item.start, item.stop, item.step        

            if item.step is None:
                step = 1
            elif item.stop is None:
                stop = len(self.coords)
            elif item.start is None:
                start = 0
            return tuple(self.coords[start:stop:step])
         
        return self.coords[item]
    
    def __setitem__(self, key, value):
        if not isinstance(key, (int, slice)):
            raise IndexError
        if isinstance( key, int ) and ( key < 0 or key >= len(self.coords) ):
            raise IndexError

        if isinstance( key, slice ):
            start, stop, step = key.start, key.stop, key.step        

            if key.step is None:
                step = 1
            elif key.stop is None:
                stop = len(self.coords)
            elif key.start is None:
                start = 0
            
            self.coords[start:stop:step] = [ element for element in value ]

        self.coords[key] = value
        return self

v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
print(v[::2])
v[0] = 10.5

