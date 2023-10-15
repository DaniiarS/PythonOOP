class Morph:

    def __init__(self, *args):
        self.words = [ arg.lower() for arg in args ]
    
    def add_word(self, word):
        if isinstance(word, str) and word not in self.words:
            self.words.append(word)
    
    def get_words(self):
        return tuple(self.words)
    
    def __eq__(self, other):
        if other.lower() in self.words:
            return True
        
        return False
    
    def __ne__(self, other):
        if other.lower() not in self.words:
            return True
        
        return False

def modify( sentence ):
    symbols = '–?!,.;'
    s = " "

    for char in sentence:
        if char not in symbols:
            s = s + char
    
    return s.split()
def count_words( dict_words ):
    count = 0
    for word in dict_words:
        for target in text:
            if target == word:
                count += 1
    return count

dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'
                        ),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'
                        ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                                 )]

text = input()
text = modify(text)

count = count_words(dict_words)

print( count )