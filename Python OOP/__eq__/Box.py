class Box:
    
    def __init__(self):
        self.things = []
    
    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self.things.append( obj )
    
    def get_things(self):
        return self.things
    
    def __eq__(self, other):
        if isinstance(other, Box):
            if len(self.get_things()) != len(other.get_things()):
                return False

            for thing in self.get_things():
                if thing not in other.get_things():
                    return False
        return True

class Thing:
    
    def __init__(self, name, mass):
        self.__name = name
        self.__mass = mass
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance( value, str ):
            self.__name = value
    
    @property
    def mass(self):
        return self.__mass
    
    @mass.setter
    def mass(self, value):
        if isinstance(value, (int, float)):
            self.__mass = value
    
    def __eq__(self, other):
        if isinstance(other, Thing):
            return self.name.lower() == other.name.lower() and self.mass == other.mass
    
    def __ne__(self, other):
        if isinstance(other, Thing):
            return not (self == other)



b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True

print( res )
print( "The last line was  added using vim editor" )
print("This line was too")
