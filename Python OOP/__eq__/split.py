stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

def modify(stich):
    symbols = '–?!,.;'
    
    modified = []
    for i in range(len(stich)):
        s = ''
        for j in range(len(stich[i])):
            if stich[i][j] not in symbols:
                s = s + stich[i][j]
        
        modified.append(s.split())
    
    return modified

class StringText:

    def __init__(self, lst_words):
        self.lst = lst_words
        self.length = len(lst_words)
    
    def __gt__(self, other):
        return self.length > other.length
    
    def __lt__(self, other):
        return self.length < other.length
    
    def __ge__(self, other):
        return self.length >= other.length
    
    def __le__(self, other):
        return self.length <= other.length


words = modify(stich)
lst_text = [ StringText(word) for word in words ]        

lst_text_sorted = sorted(lst_text, key = lambda x: x.length)

for i in range(len(lst_text_sorted)):
    lst_text_sorted[i] = " ".join(lst_text_sorted[i].lst)
