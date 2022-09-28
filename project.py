from turtle import back, up
from pico2d import *

os.getcwd()
os.chdir('c:\\Users\\user\\Desktop\\tcu\\2-2\\2DGP\\2DProject')
open_canvas(1536, 960)
back_ground = load_image('Asset1\\artwork\\Environment\\back.png')
tiles = load_image('Asset1\\artwork\\Environment\\dirt.png')
player_run1 = load_image('Asset1\\artwork\\Sprites\\player\\run\\player-run-1.png')
player_run2 = load_image('Asset1\\artwork\\Sprites\\player\\run\\player-run-2.png')
player_run3 = load_image('Asset1\\artwork\\Sprites\\player\\run\\player-run-3.png')
player_run4 = load_image('Asset1\\artwork\\Sprites\\player\\run\\player-run-4.png')
player_run5 = load_image('Asset1\\artwork\\Sprites\\player\\run\\player-run-5.png')
player_run6 = load_image('Asset1\\artwork\\Sprites\\player\\run\\player-run-6.png')
player_jump1 = load_image('Asset1\\artwork\\Sprites\\player\\jump\\player-jump-1.png')
player_jump2 = load_image('Asset1\\artwork\\Sprites\\player\\jump\\player-jump-2.png')

def draw_back():
    back_ground.clip_draw(0, 0, 384, 240, 768, 480, 1536, 960)
    tiles.clip_draw(0, 140, 469, 313, 120, 53, 240, 106)
    tiles.clip_draw(0, 140, 469, 313, 360, 53, 240, 106)
    tiles.clip_draw(0, 140, 469, 313, 600, 53, 240, 106)
    tiles.clip_draw(0, 140, 469, 313, 840, 53, 240, 106)
    tiles.clip_draw(0, 140, 469, 313, 1080, 53, 240, 106)
    tiles.clip_draw(0, 140, 469, 313, 1320, 53, 240, 106)
    tiles.clip_draw(0, 140, 469, 313, 1560, 53, 240, 106)

def player_run(x, y):
    player_run1.clip_draw(0, 0, 32, 32, x, y, 192, 192)
    delay(0.06)
    player_run2.clip_draw(0, 0, 32, 32, x, y, 192, 192)
    delay(0.06)
    player_run3.clip_draw(0, 0, 32, 32, x, y, 192, 192)
    delay(0.06)
    player_run4.clip_draw(0, 0, 32, 32, x, y, 192, 192)
    delay(0.06)
    player_run5.clip_draw(0, 0, 32, 32, x, y, 192, 192)
    delay(0.06)
    player_run6.clip_draw(0, 0, 32, 32, x, y, 192, 192)
    delay(0.06)

x, y = 400, 203
draw_back()
player_run(x, y)
update_canvas()
delay (2)
close_canvas()
