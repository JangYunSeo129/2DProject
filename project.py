from pico2d import *
import os

os.getcwd()
os.chdir('c:\\Users\\user\\Desktop\\tcu\\2-2\\2DGP\\2DProject')
back_ground = pico2d.load_image('background.png')
player_sheet = load_image('player_sheet.png')
enemy1_sheet = load_image('enemy1_sheet.png')

open_canvas(1920, 1080)

x, y = 400, 300
def player_run(x, y):
    for frame in range(6):
        player_sheet.clip_draw(frame * 33, 32, 33, 32, x, y, 264, 256)
        update_canvas()
        delay(0.06)
        clear_canvas()

def player_moveR(x, y):
    for frame in range(6):
        x = x + 35
        player_sheet.clip_draw(frame * 33, 32, 33, 32, x, y, 264, 256)
        update_canvas()
        delay(0.06)
        clear_canvas()
    return x

def player_moveL(x, y):
    for frame in range(6):
        x = x - 35
        player_sheet.clip_draw(frame * 33, 32, 33, 32, x, y, 264, 256)
        update_canvas()
        delay(0.06)
        clear_canvas()
    return x

def player_jump(x, y):
    for i in range(5):
        y = y + 71
        player_sheet.clip_draw(0, 0, 33, 32, x, y, 264, 256)
        update_canvas()
        delay(0.06)
        clear_canvas()
    for i in range(3):
        y = y - 33
        player_sheet.clip_draw(33, 0, 32, 32, x, y, 264, 256)
        update_canvas()
        delay(0.06)
        clear_canvas()
    return y

def player_down(x, y):
    for i in range(8):
        player_sheet.clip_draw(33, 0, 33, 32, x, y, 264, 256)
        update_canvas()
        delay(0.06)
        y = y - 32
        clear_canvas()
    return y

y = player_jump(x, y)
player_run(x, y)

close_canvas()
