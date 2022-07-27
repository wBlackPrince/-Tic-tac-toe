from cgitb import enable
from ursina import *
from random import randint

#? класс игрового поля
class GameField:
    c = 0

    #? генерация игрового поля
    def __init__(self,coords):
        self.enable = False
        self.field = [[Cage(*coords[i][j]) for j in range(3)] for i in range(3)]
        self.win = False
        self.c = 1
    
    #? ход компьютера
    def computer_go(self):
        while True:
            i,j = randint(0,2),randint(0,2)
            if self.field[i][j].value == 'free':
                break
        self.field[i][j].icon = 'Zero.png'
        self.field[i][j].value = 'nofree'
        self.field[i][j].owner = 2
    
    #? проверка на заполненность
    def check_full(self):
        mas = self.field
        full_mas = []
        for i in range(3):
            matr = [True for j in range(3) if mas[i][j].value == 'free']
            full_mas.extend(matr)
        return any(full_mas)

    #? проверка вертикалей
    def check_vertic(self):
        mas = self.field
        for i in range(3):
            if mas[0][i].owner == mas[1][i].owner == mas[2][i].owner == 2:
                return 'computer'
            elif mas[0][i].owner == mas[1][i].owner == mas[2][i].owner == 1:
                return 'human'
    
    #? проверка горизонталей
    def check_horizon(self):
        mas = self.field
        for i in range(3):
            if mas[i][0].owner == mas[i][1].owner == mas[i][2].owner == 2:
                return 'computer'
            elif mas[i][0].owner == mas[i][1].owner == mas[i][2].owner == 1:
                return 'human'
    
    #? проверка диагоналей
    def check_diagonal(self):
        mas = self.field
        if mas[2][0].owner == mas[1][1].owner == mas[0][2].owner:
            if mas[2][0].owner == 1:
                return 'human'
            elif mas[2][0].owner == 2:
                return 'computer'
        elif mas[0][0].owner == mas[1][1].owner == mas[2][2].owner:
            if mas[0][0].owner == 1:
                return 'human'
            elif mas[0][0].owner == 2:
                return 'computer'
    
    #? проверка на победу
    def check_win(self):
        d = self.check_diagonal()
        h = self.check_horizon()
        v = self.check_vertic()

        #? определиться победитель среди d,h и v
        winner = None
        f = self.check_full()

        if d != None:
            winner = d
        elif h != None:
            winner = h
        elif v != None:
            winner = v
        #? ничья
        elif f == False:
            winner = 'pat'
        else:
            return None
        
        return winner



#? класс клетки
class Cage(Button):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.scale = .1
        self.color = color.white
        self.value = 'free'
        #? под чьим контолем клетка: 1-человек, 2-компьютер
        self.owner = None
    
    #? c- это счетчик, если четный то ходит человек
    def action(self):
        if GameField.c %2 == 0:
            self.icon = 'krest.png'
            self.value = 'nofree'
            GameField.c+=1
            self.owner = 1


