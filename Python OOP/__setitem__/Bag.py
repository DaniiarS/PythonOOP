class Thing:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Bag:
    
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.current_weight = 0
        self.things = []
    
    def add_thing(self, thing):
        if not isinstance(thing, Thing):
            raise ValueError
        
        if self.max_weight < self.current_weight + thing.weight:
            raise ValueError('превышен суммарный вес предметов')

        self.things.append( thing )
        self.current_weight += thing.weight
    
    def __getitem__(self, index):
        if not isinstance(index, int) or ( index < 0 or index >= len(self.things)):
            raise IndexError

        return self.things[index]
    
    def __setitem__(self, key, value):
        if not isinstance(value, Thing):
            raise ValueError
        
        if not isinstance(key, int) or (key < 0 or key >= len(self.things)):
            raise IndexError
        
        if self.max_weight < self.current_weight + value.weight - self.things[key].weight:
            raise ValueError('превышен суммарный вес предметов')
        self.current_weight += (value.weight - self.things[key].weight)
        self.things[key] = value
        return self

    def __delitem__(self, index):
        if not isinstance(index, int) or ( index < 0 or index >= len(self.things)):
            raise IndexError
        
        self.current_weight -= self.things[index].weight
        del self.things[index]
        return self

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))
try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"
t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"
del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"
try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
    
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))
b[0] = Thing('рубашка', 500)
try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
 