import game_framework
from pico2d import *
import title_state

background_image = None
gem_image = None

def enter():
    global background_image
    global gem_image
    background_image = load_image('ui_panels.png')
    gem_image = load_image('gem.png')

def exit():
    global background_image
    global gem_image
    del background_image
    del gem_image

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
    background_image.clip_draw(0, 32, 32, 32, 960, 540, 2000, 2000)
    background_image.clip_draw(0, 32, 32, 32, 960, 540, 960, 960)
    gem_image.clip_draw(0, 0, 15, 13, 700, 700, 180, 156)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass