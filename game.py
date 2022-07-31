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

def click_restart():
    global field
    for i in range(3):
        for j in range(3):
            destroy(field.field[i][j])
    field = GameField(coords)
    GameField.c = 0


#? координаты клеток поля
coords = (((-.12,.12),(0,.12),(.12,.12)),((-.12,0),(0,0),(.12,0)),((-.12,-.12),(0,-.12),(.12,-.12)))
field = GameField(coords)

#? пользовательский интерфейс
restart_game = Button(scale = (.4,.1),text = 'Exit',y = -.4,on_click = click_restart)


app.run()