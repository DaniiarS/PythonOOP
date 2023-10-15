class StackObj:
    
    def __init__(self, data):
        self.__data = data
        self.__next = None
    
    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        if obj is None:
            self.__next = None
            return
        if not isinstance(obj, (StackObj)):
            raise TypeError
        
        self.__next = obj

class Stack:

    def __init__(self):
        self.__top = None
        self.__tail = None
        self.__size = 0
    
    def push(self, obj):
        if self.__top is None:
            self.__top = obj
            self.__tail = obj
            self.__size += 1
            return
        
        self.__tail.next = obj
        self.__tail = obj
        self.__size += 1

    def pop(self):
        ptr = self.__top
        res = self.__tail

        while True:
            if( ptr.next == self.__tail ):
                ptr.next = None
                break
            ptr = ptr.next 

        self.__tail = ptr
        self.__size -= 1
        return res

    def __repr__(self):
        ptr = self.__top
        res = ""

        while ptr != None:
            res += str(ptr.data) + " "
            ptr = ptr.next
        return res
    
    def __getitem__(self, item):
        if not isinstance( item, int ) or (item < 0 or item >= self.__size ):
            raise IndexError('неверный индекс')

        ptr = self.__top

        for i in range(self.__size):
            if i == item:
                return ptr
            ptr = ptr.next
    
    def __setitem__(self, key, value):
        if not isinstance(key, int) or (key < 0 or key >= self.__size):
            raise IndexError('неверный индекс')
        
        if not isinstance( value, StackObj ):
            raise ValueError
        
        if key == self.__size - 1:
            self.pop()
            self.push(value)
            return self
            
        ptr = self.__top
        
        for i in range(self.__size):
            if i == key - 1:
                value.next = ptr.next.next
                ptr.next = value
                return self
            ptr = ptr.next

