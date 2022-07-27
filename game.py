from ursina import *
from game_clases import *

app = Ursina()


def update():
    field.field[0][0].on_click = field.field[0][0].action
    field.field[0][1].on_click = field.field[0][1].action
    field.field[0][2].on_click = field.field[0][2].action
    field.field[1][0].on_click = field.field[1][0].action
    field.field[1][1].on_click = field.field[1][1].action
    field.field[1][2].on_click = field.field[1][2].action
    field.field[2][0].on_click = field.field[2][0].action
    field.field[2][1].on_click = field.field[2][1].action
    field.field[2][2].on_click = field.field[2][2].action

    winner = field.check_win()

    if GameField.c%2 != 0 and winner == None:
        field.computer_go()
        GameField.c +=1
    
    #? проверка на победу

    winner = field.check_win()
    if winner != None:
        if winner == 'computer':
            print_on_screen('Game over',position = (0,.3),duration = .5)
        elif winner == 'human':
            print_on_screen('Win',position = (0,.3),duration = .5)
        elif winner == 'pat':
            print_on_screen('Pat',position = (0,.3),duration = .5)

    #? проверка на начало игры

    def fstart_game():
        global coords
        global field
        global start_game

        field = GameField(coords)
        destroy(start_game)
        exit_game.y = -.4
    
    #? выход в главное меню
    def fexit_game():
        global field
        global exit_game
        global start_coords
        global start_game

        exit_game.y = -12

        for i in range(len(field.field)):
            for j in range(len(field.field[i])):
                destroy(field.field[i][j])
        field = GameField(start_coords)
        start_game = Button(scale = (.4,.1),text = 'Game')


    
    start_game.on_click = fstart_game
    exit_game.on_click = fexit_game


#? начальное поле находится за пределами камеры, с началом игры формируется новое в пределах камеры
start_coords = coords = (((-12,12),(0,12),(12,12)),((12,0),(12,0),(12,0)),((12,12),(0,12),(12,12)))
field = GameField(start_coords)

#? координаты клеток поля
coords = (((-.12,.12),(0,.12),(.12,.12)),((-.12,0),(0,0),(.12,0)),((-.12,-.12),(0,-.12),(.12,-.12)))

#? пользовательский интерфейс
#? кнопка начал игры
start_game = Button(scale = (.4,.1),text = 'Game')
exit_game = Button(scale = (.4,.1),text = 'Exit',y=15)




app.run()