import game_framework
from pico2d import *
import title_state
import objects

background_image = None
gem_image = None
fox_image = None
font = None

def enter():
    global background_image
    global gem_image
    global fox_image
    global font
    background_image = load_image('ui_panels.png')
    gem_image = load_image('gem.png')
    fox_image = load_image('fox.png')
    font = load_font('ENCR10B.TTF', 200)

def exit():
    global background_image
    global gem_image
    global fox_image
    global font
    del background_image
    del gem_image
    del fox_image
    del font

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_SPACE:
                game_framework.change_state(title_state)


def draw():
    clear_canvas()
    background_image.clip_draw(0, 32, 32, 32, 960, 540, 2200, 2000)
    background_image.clip_draw(32, 32, 32, 32, 960, 540, 960, 960)
    fox_image.clip_draw(66, 0, 33, 32, 960, 810, 330, 320)
    gem_image.clip_draw(0, 0, 15, 13, 700, 500, 180, 156)
    font.draw(1000, 500, '%d' % objects.userscore, (255, 255, 0))
    
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass