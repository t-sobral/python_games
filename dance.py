# pyright: reportUndefinedVariable=false
# pgzrun

import this
from random import randint

import pgzrun

WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

move_list = []
display_list = []

score = 0
current_move = 0
count = 4
dance_length = 4

say_dance = False
show_countdown = True
moves_complete = False
game_over = False


dancer = Actor("dancer-start")
dancer.pos = CENTRE_X + 5, CENTRE_Y - 40

up = Actor("up")
up.pos = CENTRE_X, CENTRE_Y + 110

down = Actor("down")
down.pos = CENTRE_X, CENTRE_Y + 230

left = Actor("left")
left.pos = CENTRE_X - 60, CENTRE_Y + 170

right = Actor("right")
right.pos = CENTRE_X + 60, CENTRE_Y + 170


def draw():
    global game_over, score, say_dance
    global count, show_countdown

    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        screen.draw.text("score: " + str(score), color="black", topleft=(10, 10))

    return


def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        up.image = "up"
        right.image = "right"
        down.image = "down"
        left.image = "left"
    return


def update_dancer(move):
    global game_over

    if not game_over:
        if move == 0:
            up.image = "up-lit"
            dancer.image = "dancer-up"
            clock.schedule(reset_dancer, 0.5)

        elif move == 1:
            right.image = "right-lit"
            dancer.image = "dancer-right"
            clock.schedule(reset_dancer, 0.5)

        elif move == 2:
            down.image = "down-lit"
            dancer.image = "dancer-down"
            clock.schedule(reset_dancer, 0.5)

        else:
            left.image = "left-lit"
            dancer.image = "dancer-left"
            clock.schedule(reset_dancer, 0.5)

        return


def display_moves():
    global move_list, display_list, dance_length
    global say_dance, show_countdown, current_move

    if display_list:
        this_move = display_list[0]
        display_list = display_list[1:]
        if this_move == 0:
            update_dancer(0)
            clock.schedule(display_moves, 1)
        elif this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves, 1)
        elif this_move == 2:
            update_dancer(2)
            clock.schedule(display_moves, 1)
        else:
            update_dancer(3)
            clock.schedule(display_moves, 1)
    else:
        say_dance = True
        show_countdown = False

    return


def generate_moves():
    pass


def countdown():
    pass


def next_move():
    pass


def on_key_up(key):
    global score, game_over, move_list, current_move
    if key == keys.UP:
        update_dancer(0)
    elif key == keys.RIGHT:
        update_dancer(1)
    elif key == keys.DOWN:
        update_dancer(2)
    elif key == keys.LEFT:
        update_dancer(3)
    return


def update():
    pass


pgzrun.go()
