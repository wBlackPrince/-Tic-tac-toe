from ursina import *
from random import randint

#? класс игрового поля
class GameField:
    c = 0

    #? генерация игрового поля
    def __init__(self,coords,**kwargs):
        self.enable = False
        self.field = [[Cage(*coords[i][j]) for j in range(3)] for i in range(3)]
        self.win = False
    
    #? ход компьютера
    def computer_go(self):
        while True:
            i,j = randint(0,2),randint(0,2)
            if self.field[i][j].value == 'free':
                break
        self.field[i][j].icon = 'Zero.png'
        self.field[i][j].value = 'nofree'
        self.field[i][j].owner = 2
        self.field[i][j].click = False
        GameField.c += 1
    
    #? проверка на заполненность
    def check_full(self):
        mas = self.field
        full_mas = []
        for i in range(3):
            matr = [True for j in range(3) if mas[i][j].value == 'free']
            full_mas.extend(matr)
        return any(full_mas)


    def checker(self):
        mas = self.field
        won = (
                (mas[0][0].owner == mas[0][1].owner == mas[0][2].owner != None, mas[0][0].owner),#? проверка горизонталей
                (mas[1][0].owner == mas[1][1].owner == mas[1][2].owner != None, mas[1][0].owner),
                (mas[2][0].owner == mas[2][1].owner == mas[2][2].owner != None, mas[2][0].owner),
                (mas[0][0].owner == mas[1][0].owner == mas[2][0].owner != None, mas[0][0].owner),#? проверка вертикалей
                (mas[0][1].owner == mas[1][1].owner == mas[2][1].owner != None, mas[0][1].owner),
                (mas[0][2].owner == mas[1][2].owner == mas[2][2].owner != None, mas[0][2].owner),
                (mas[0][0].owner == mas[1][1].owner == mas[2][2].owner != None, mas[0][0].owner),#? проверка главной диагонали
                (mas[2][0].owner == mas[1][1].owner == mas[0][2].owner != None, mas[1][1].owner))#? проверка побочной диагонали
        for i in won:
            if i[0]:
                return i[1]
        return None

    #? проверка на победу
    def check_win(self):
        winner = self.checker()

        if winner != None:
            return winner
        #? ничья
        elif not(self.check_full()):
            return 3
        else:
            return None

#? класс клетки
class Cage(Button):
    def __init__(self,x,y):
        super().__init__(x = x,y = y,scale = .1,color = color.white,on_click = self.action)

        self.value = 'free'
        #? под чьим контолем клетка: 1-человек, 2-компьютер
        self.owner = None
        #? можно ли нажать на кнопку
        self.click = True
    
    #? c- это счетчик, если четный то ходит человек
    def action(self):
        if GameField.c %2 == 0 and self.click:
            self.icon = 'Cross.png'
            self.value = 'nofree'
            GameField.c+=1
            self.owner = 1
            self.click = False



