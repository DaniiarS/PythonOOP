class FileAcceptor:
    
    def __init__(self, *args):
        self.extensions = self.traverse(args)
    
    @staticmethod
    def traverse(myList):
        result = []
        for arg in myList:
            if isinstance(arg, list):
                for element in arg:
                    result.append(element)
            else:
                result.append(arg)
        
        return result

    def __call__(self, filename):
        filename = filename.split(".")[-1]
        
        if filename in self.extensions:
            return True
        
        return False
    
    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            return FileAcceptor( self.extensions + other.extensions )

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor3 = acceptor1 + acceptor2

filtered = list(filter(acceptor1, filenames))
print(filtered)

print(acceptor3.extensions)