class Body:

    def __init__(self, name, ro, volume):
        self.__name = name
        self.__ro = ro
        self.__volume = volume
        self.__mass = ro * volume
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance( value, str ):
            self.__name = value
    
    @property
    def ro(self):
        return self.__ro
    
    @ro.setter
    def ro(self, value):
        if isinstance( value, (int, float) ):
            self.__ro = value
    
    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, value):
        if isinstance( value, (int, float) ):
            self.__volume = value
    

    def __eq__(self, other):
        if isinstance( other, Body ):
            return self.mass == other.__mass
        elif isinstance( other, (int, float) ):
            return self.mass == other
    
    def __gt__(self, other):
        if isinstance( other, Body ):
            return self.mass > other.mass
        elif isinstance( other, (int, float ) ):
            return self.mass > other
    
    def __lt__(self, other):
        if isinstance( other, Body ):
            return self.mass < other.mass
        elif isinstance( other, (int, float) ):
            return self.mass < other
         