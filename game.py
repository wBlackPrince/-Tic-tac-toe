from cgitb import enable
from ursina import *
from game_clases import *

app = Ursina()
window.fullscreen = True

def update():
    winner = field.check_win()

    if GameField.c%2 != 0 and winner == None:
        field.computer_go()

    #? проверка на победу

    winner = field.check_win()
    if winner != None:
        if winner == 2:
            print_on_screen('Game over',position = (0,.3),duration = .5)
        elif winner == 1:
            print_on_screen('Win',position = (0,.3),duration = .5)
        elif winner == 3:
            print_on_screen('Pat',position = (0,.3),duration = .5)


#? проверка на начало игры
def fstart_game():
    global field

    for i in range(3):
        for j in range(3):
            field.field[i][j].enabled = True
    
    start_game.enabled = False
    exit_game.enabled = True


#? выход в главное меню
def fexit_game():
    global field

    exit_game.enabled = False

    for i in range(3):
        for j in range(3):
            destroy(field.field[i][j])
    field = GameField(coords,enabled = False)

    start_game.enabled = True
    GameField.c = 0


#? координаты клеток поля
coords = (((-.12,.12),(0,.12),(.12,.12)),((-.12,0),(0,0),(.12,0)),((-.12,-.12),(0,-.12),(.12,-.12)))
field = GameField(coords,enabled = False)

#? пользовательский интерфейс
#? кнопка начал игры
start_game = Button(scale = (.4,.1),text = 'Game',on_click = fstart_game)
exit_game = Button(scale = (.4,.1),text = 'Exit',y = -.4,enabled = False,on_click = fexit_game)


app.run()