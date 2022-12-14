from pico2d import *
import game_framework
import title_state

image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')

def exit():
    global image
    del image

def update():
    global logo_time
    
    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.02

def draw():
    clear_canvas()
    image.clip_draw(0, 0, 800, 600, 960, 540, 1920, 1080)
    update_canvas()

def handle_events():
    events = get_events()