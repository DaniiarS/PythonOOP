import sys

class ValidateNumber:    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.isvalid(value):
            if type(value) is str:
                if '.' in value:
                    instance.__dict__[self.name] = float(value)
                else:
                    instance.__dict__[self.name] = int(value)
            elif type(value) is float:
                instance.__dict__[self.name] = float(value)
            else:
                instance.__dict__[self.name] = int(value)

            
    
    @classmethod
    def isvalid(cls, value):
        if isinstance(value, (int, float)):
            return True

        dot = 0
        digits = '0123456789'
        
        # Chekc if the value is 0 or starts with 0
        if value[0] == '0':
            if len(value) == 1:
                return True
            
            return False
        
        #Validate the value
        for digit in value:
            if dot == 2:
                return False

            if digit == '.':
                dot += 1
                continue
            
            if digit not in digits:
                return False
        
        return True
            


class ValidateString:
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.isvalid(value):
            instance.__dict__[self.name] = value
    
    @classmethod
    def isvalid(cls, value):
        return type(value) is str

class ShopItem:
    name = ValidateString()
    weight = ValidateNumber()
    price = ValidateNumber()

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
    
    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash( (self.name.lower(), self.weight, self.price) )
    

lst_in = list(map( str.strip, sys.stdin.readlines()))
shop_items = {}

for item in lst_in:
    name, quants = item.split(':')
    weight, price = quants.split()

    item_obj = ShopItem(name, weight, price)
    
    if item_obj in shop_items:
        shop_items[item_obj][-1] += 1
    else:
        shop_items[item_obj] = [item_obj, 1]

print( shop_items )
# it1 = ShopItem('name', 10, 11)