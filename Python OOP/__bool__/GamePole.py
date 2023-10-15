from random import randint

class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, N, M, total_mines):
        self.__pole_cells = []
        self.N = N
        self.M = M
        self.total_mines = total_mines

    @property
    def pole(self):
        return self.__pole_cells
    
    def init_pole(self):
        self.__pole_cells = [ [Cell() for i in range(self.M)] for j in range(self.N) ]
        
        mines = self.total_mines

        while mines != 0:
            i, j = randint(0, self.N - 1), randint(0, self.M - 1)
            if not self.__pole_cells[i][j].is_mine:
                self.__pole_cells[i][j].is_mine = True
                mines -= 1
        
        # Check the edges of the Pole ...
        if self.__pole_cells[0][1].is_mine:
            self.__pole_cells[0][0].number += 1
        if self.__pole_cells[1][1].is_mine:
            self.__pole_cells[0][0].number += 1
        if self.__pole_cells[1][0].is_mine:
            self.__pole_cells[0][0].number += 1
        
        if self.__pole_cells[0][-2].is_mine:
            self.__pole_cells[0][-1].number += 1
        if self.__pole_cells[1][-2].is_mine:
            self.__pole_cells[0][-1].number += 1
        if self.__pole_cells[1][-1].is_mine:
            self.__pole_cells[0][-1].number += 1
        
        if self.__pole_cells[-2][0].is_mine:
            self.__pole_cells[-1][0].number += 1
        if self.__pole_cells[-2][1].is_mine:
            self.__pole_cells[-1][0].number += 1
        if self.__pole_cells[-1][1].is_mine:
            self.__pole_cells[-1][0].number += 1
        
        if self.__pole_cells[-2][-2].is_mine:
            self.__pole_cells[-1][-1].number += 1
        if self.__pole_cells[-2][-1].is_mine:
            self.__pole_cells[-1][-1].number += 1
        if self.__pole_cells[-1][-2].is_mine:
            self.__pole_cells[-1][-1].number += 1
        
        #Check the bottom border
        for i in range(1, self.M - 1):
            if self.__pole_cells[0][i - 1].is_mine:
                self.__pole_cells[0][i].number += 1
            elif self.__pole_cells[0][i + 1].is_mine:
                self.__pole_cells[0][i].number += 1
            elif self.__pole_cells[1][i - 1].is_mine:
                self.__pole_cells[0][i].number += 1
            elif self.__pole_cells[1][i].is_mine:
                self.__pole_cells[0][i].number += 1
            elif self.__pole_cells[1][i + 1].is_mine:
                self.__pole_cells[0][i].number += 1

        #Check the top border
        for i in range(1, self.M - 1):
            if self.__pole_cells[-1][i - 1].is_mine:
                self.__pole_cells[-1][i].number += 1
            if self.__pole_cells[-1][i + 1].is_mine:
                self.__pole_cells[-1][i].number += 1
            if self.__pole_cells[-2][i - 1].is_mine:
                self.__pole_cells[-1][i].number += 1
            if self.__pole_cells[-2][i].is_mine:
                self.__pole_cells[-1][i].number += 1
            if self.__pole_cells[-2][i + 1].is_mine:
                self.__pole_cells[-1][i].number += 1
        
        #Check the left border
        for i in range(1, self.N - 1):
            if self.__pole_cells[i-1][0].is_mine:
                self.__pole_cells[i][0].number += 1
            if self.__pole_cells[i-1][1].is_mine:
                self.__pole_cells[i][0].number += 1
            if self.__pole_cells[i + 1][0].is_mine:
                self.__pole_cells[i][0].number += 1
            if self.__pole_cells[i +1][1].is_mine:
                self.__pole_cells[i][0].number += 1
            if self.__pole_cells[i][1].is_mine:
                self.__pole_cells[i][0].number += 1
        
        #Check the right border
        for i in range(1, self.N - 1):
            if self.__pole_cells[i - 1][-1].is_mine:
                self.__pole_cells[i][-1].number += 1
            if self.__pole_cells[i - 1][-2].is_mine:
                self.__pole_cells[i][-1].number += 1
            if self.__pole_cells[i + 1][-1].is_mine:
                self.__pole_cells[i][-1].number += 1
            if self.__pole_cells[i + 1][-2].is_mine:
                self.__pole_cells[i][-1].number += 1
            if self.__pole_cells[i][-2].is_mine:
                self.__pole_cells[i][-1].number += 1
        
        #Check the Pole in general
        for i in range(1, self.N - 1):
            for j in range(1, self.M - 1):
                for k in range(3):
                    if self.__pole_cells[i + 1][j + k - 1].is_mine:
                        self.__pole_cells[i][j].number += 1
                    if self.__pole_cells[i - 1][j + k - 1].is_mine:
                        self.__pole_cells[i][j].number += 1
                if self.__pole_cells[i][j - 1].is_mine:
                    self.__pole_cells[i][j].number += 1
                if self.__pole_cells[i][j + 1].is_mine:
                    self.__pole_cells[i][j].number += 1
    
    # Opens the closed cell in the Pole
    def open_cell(self, i, j):
        if (i >= self.N or i < 0) or (j >= self.M or j < 0):
            raise IndexError('некорректные индексы i, j клетки игрового поля')

        self.__pole_cells[i][j].is_open = True
    
    # Prints the whole Pole
    def show_pole(self):
        for row in self.pole:
            for element in row:
                if element.is_open:
                    print(" 1 ", end = " ")
                else:
                    print(" 0 ", end = " ")
            print()
            
class Cell:
    
    def __init__(self, is_mine = False, number = 0, is_open = False):
        self.__is_mine = is_mine
        self.__number = number
        self.__is_open = is_open
    
    @property
    def is_mine(self):
        return self.__is_mine
    
    @is_mine.setter
    def is_mine(self, flag):
        if type(flag) is not bool:
            raise ValueError("недопустимое значение атрибута")

        self.__is_mine = flag
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        if (value is int):
            self.__number = value
        if self.__number > 8 or self.__number < 0:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open
    
    @is_open.setter
    def is_open(self, flag):
        if type(flag) is not bool:
            raise ValueError("недопустимое значение атрибута")

        self.__is_open = flag
    
    def __bool__(self):
        return self.is_open

pole = GamePole(5, 5, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if not pole.pole[0][1]:
    pole.open_cell(0, 1)
if not pole.pole[3][4]:
    pole.open_cell(3, 4)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()