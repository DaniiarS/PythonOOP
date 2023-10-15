class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    @classmethod
    def is_valid(cls, value):
        return isinstance(value, (int, float)) and value >= cls.MIN_DIMENSION and value <= cls.MAX_DIMENSION
    
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, value):
        if not self.is_valid(value):
            raise ValueError
        
        self.__a = value
    
    @property
    def b(self):
        return self.__b
    
    @b.setter
    def b(self, value):
        if not self.is_valid(value):
            raise ValueError
        
        self.__b = value
    
    @property
    def c(self):
        return self.__c
    
    @c.setter
    def c(self, value):
        if not self.is_valid(value):
            raise ValueError
        
        self.__c = value
    
    def volume(self):
        return self.a * self.b * self.c

    def __ge__(self, other):
        return self.volume >= other.volume

    def __le__(self, other):
        return self.volume <= other.volume
    
    def __gt__(self, other):
        return self.volume > other.volume
    
    def __lt__(self, other):
        return self.volume < other.volume
    
class ShopItem:

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim
        self.volume =Dimensions(dim[0], dim[1], dim[2]).volume()
    

item1 = ShopItem( "кеды", 1024, (40, 30, 120) )
item2 = ShopItem( "зонт", 500.24,  (10, 20, 50) )
item3 = ShopItem( "холодильник", 40000, (2000, 600, 500) )
item4 = ShopItem( "табуретка", 2000.99, (500, 200, 200) ) 


lst_shop = ( item1, item2, item3, item4 )
lst_shop_sorted = sorted(lst_shop, key= lambda x: x.volume )

# for item in lst_shop_sorted:
#     print(item.name)

# for item in lst_shop:
#     print( item.name )