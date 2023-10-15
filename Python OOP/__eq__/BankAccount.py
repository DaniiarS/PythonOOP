class CentralBank:
    
    def __new__(cls, *args, **kwargs):
        return None
    
    def __init__(self):
        return None
        
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    @classmethod
    def register(cls, money):
        money.cb = cls
    
class MoneyR:

    def __init__(self, amount = 0):
        self.__cb = None
        self.__volume = amount
        self.currency_name = 'rub'
    
    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, bank):
        if type(bank) == type(CentralBank):
            self.__cb = bank
    
    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, amount):
        if isinstance(amount, (float, int)) and amount >=0:
            self.__volume = amount

    def __gt__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return self.cb.rates[self.currency_name] * self.volume > (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']

    def __lt__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return self.cb.rates[self.currency_name] * self.volume < (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']

    def __ge__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return self.cb.rates[self.currency_name] * self.volume >= (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']
    
    def __le__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return self.cb.rates[self.currency_name] * self.volume <= (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']
    
    def __eq__(self, other):
        if isinstance(other, (MoneyR, MoneyD, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return abs(self.volume - (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']) <= 0.1

class MoneyD:

    def __init__(self, amount = 0):
        self.__cb = None
        self.__volume = amount
        self.currency_name = 'dollar'
    
    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, bank):
        if type(bank) == type(CentralBank):
            self.__cb = bank
    
    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, amount):
        if isinstance(amount, (float, int)) and amount >=0:
            self.__volume = amount

    def __gt__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return self.cb.rates['rub'] * self.volume > (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']

    def __lt__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return self.cb.rates['rub'] * self.volume < (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']

    def __ge__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return self.cb.rates['rub'] * self.volume >= (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']
    
    def __le__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return self.cb.rates['rub'] * self.volume <= (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']
    
    def __eq__(self, other):
        if isinstance(other, (MoneyR, MoneyD, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return abs((self.volume/self.cb.rates[self.currency_name]) * self.cb.rates['rub'] - (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']) <= 0.1


class MoneyE:

    def __init__(self, amount = 0):
        self.__cb = None
        self.__volume = amount
        self.currency_name = 'euro'
    
    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, bank):
        if type(bank) == type(CentralBank):
            self.__cb = bank
    
    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, amount):
        if isinstance(amount, (float, int)) and amount >=0:
            self.__volume = amount

    def __gt__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return (self.volume/self.cb.rates[self.currency_name]) * self.cb.rates['rub'] > (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']

    def __lt__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return (self.volume/self.cb.rates[self.currency_name]) * self.cb.rates['rub'] < (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']

    def __ge__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return (self.volume/self.cb.rates[self.currency_name]) * self.cb.rates['rub'] >= (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']
    
    def __le__(self, other):
        if isinstance(other, (MoneyD, MoneyR, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return (self.volume/self.cb.rates[self.currency_name]) * self.cb.rates['rub'] <= (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']
    
    def __eq__(self, other):
        if isinstance(other, (MoneyR, MoneyD, MoneyE)):
            if other.cb == None:
                raise ValueError("Неизвестен курс валют.")
            return abs((self.volume/self.cb.rates[self.currency_name]) * self.cb.rates['rub'] - (other.volume/other.cb.rates[other.currency_name]) * other.cb.rates['rub']) <= 0.1