import game_framework
from pico2d import *
import play_state

background_image = None
ui_image = None
user_select = None

def enter():
    global background_image
    global ui_image
    global user_select
    background_image = load_image('tuk_credit.png')
    ui_image = load_image('ui_large.png')
    user_select = 'start_game'

def exit():
    global background_image
    global ui_image
    global user_select
    del background_image
    del ui_image
    del user_select

def handle_events():
    global user_select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_DOWN:
                user_select = 'exit_game'
            elif event.key == SDLK_UP:
                user_select = 'start_game'
            elif event.key == SDLK_SPACE:
                if user_select == 'start_game':
                    game_framework.change_state(play_state)
                elif user_select == 'exit_game':
                    game_framework.quit()

def draw():
    global user_select
    clear_canvas()
    background_image.clip_draw(0, 0, 800, 600, 960, 540, 1920, 1080)
    if user_select == 'start_game':
        ui_image.clip_draw(144, 32, 48, 16, 930, 300, 480, 160)
        ui_image.clip_draw(288, 32, 48, 16, 930, 130, 480, 160)
    elif user_select == 'exit_game':
        ui_image.clip_draw(96, 32, 48, 16, 930, 300, 480, 160)
        ui_image.clip_draw(336, 32, 48, 16, 930, 130, 480, 160)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass