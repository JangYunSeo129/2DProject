import game_framework
from pico2d import *
import play_state

background_image = None
ui_image = None
fox_image = None
user_select = None
frame = None
bgm = None
choose_bgm = None
select_bgm = None

def enter():
    global background_image
    global ui_image
    global user_select
    global fox_image
    global frame
    global bgm
    global choose_bgm
    global select_bgm
    background_image = load_image('ui_panels.png')
    ui_image = load_image('ui_large.png')
    fox_image = load_image('fox.png')
    user_select = 'start_game'
    frame = 0
    bgm = load_music('title.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()
    choose_bgm = load_music('choose.mp3')
    select_bgm = load_music('select.mp3')
    choose_bgm.set_volume(32)
    select_bgm.set_volume(32)

def exit():
    global background_image
    global ui_image
    global user_select
    global fox_image
    global frame
    global bgm
    global choose_bgm
    global select_bgm
    del background_image
    del ui_image
    del user_select
    del fox_image
    del frame
    del bgm
    del choose_bgm
    del select_bgm

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
                choose_bgm.play()
                user_select = 'exit_game'
            elif event.key == SDLK_UP:
                choose_bgm.play()
                user_select = 'start_game'
            elif event.key == SDLK_SPACE:
                select_bgm.play()
                if user_select == 'start_game':
                    game_framework.change_state(play_state)
                elif user_select == 'exit_game':
                    game_framework.quit()

def draw():
    global user_select
    clear_canvas()
    background_image.clip_draw(0, 32, 32, 32, 960, 540, 2200, 2000)
    if user_select == 'start_game':
        ui_image.clip_draw(144, 32, 48, 16, 930, 300, 480, 160)
        ui_image.clip_draw(288, 32, 48, 16, 930, 130, 480, 160)
    elif user_select == 'exit_game':
        ui_image.clip_draw(96, 32, 48, 16, 930, 300, 480, 160)
        ui_image.clip_draw(336, 32, 48, 16, 930, 130, 480, 160)
    fox_image.clip_draw(frame * 33, 32, 33, 32, 930, 700, 330, 320)
    update_canvas()
    delay(0.06)

def update():
    global frame
    frame = (frame + 1) % 6

def pause():
    pass

def resume():
    pass