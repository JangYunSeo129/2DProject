from pico2d import *
import game_framework
import title_state
import play_state


background_image = None
ui_image = None
user_select = None
choose_bgm = None
select_bgm = None

def enter():
    global background_image
    global ui_image
    global user_select
    global choose_bgm
    global select_bgm
    background_image = load_image('ui_panels.png')
    ui_image = load_image('ui_small.png')
    user_select = 'resume_game'
    choose_bgm = load_music('choose.mp3')
    select_bgm = load_music('select.mp3')
    choose_bgm.set_volume(32)
    select_bgm.set_volume(32)


def exit():
    global background_image
    global ui_image
    global user_select
    global choose_bgm
    global select_bgm
    del background_image
    del ui_image
    del user_select
    del choose_bgm
    del select_bgm

def draw():
    global user_select
    clear_canvas()
    play_state.draw_world()
    background_image.clip_draw(0, 32, 32, 32, 960, 540, 960, 960)
    ui_image.clip_draw(144, 224, 16, 16, 960, 800, 320, 320)
    if user_select == 'resume_game':
        ui_image.clip_draw(80, 240, 16, 16, 700, 350, 160, 160)
        ui_image.clip_draw(64, 144, 16, 16, 960, 350, 160, 160)
        ui_image.clip_draw(64, 48, 16, 16, 1220, 350, 160, 160)
    elif user_select == 'home':
        ui_image.clip_draw(64, 240, 16, 16, 700, 350, 160, 160)
        ui_image.clip_draw(80, 144, 16, 16, 960, 350, 160, 160)
        ui_image.clip_draw(64, 48, 16, 16, 1220, 350, 160, 160)
    elif user_select == 'exit_game':
        ui_image.clip_draw(64, 240, 16, 16, 700, 350, 160, 160)
        ui_image.clip_draw(64, 144, 16, 16, 960, 350, 160, 160)
        ui_image.clip_draw(80, 48, 16, 16, 1220, 350, 160, 160)
    update_canvas()

def handle_events():
    global user_select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_LEFT:
                choose_bgm.play()
                if user_select == 'exit_game':
                    user_select = 'home'
                elif user_select == 'home':
                    user_select = 'resume_game'
            elif event.key == SDLK_RIGHT:
                choose_bgm.play()
                if user_select == 'resume_game':
                    user_select = 'home'
                elif user_select == 'home':
                    user_select = 'exit_game'
            elif event.key == SDLK_SPACE:
                select_bgm.play()
                if user_select == 'resume_game':
                    game_framework.pop_state()
                elif user_select == 'home':
                    game_framework.change_state(title_state)
                elif user_select == 'exit_game':
                    game_framework.quit()

def update():
    pass

def pause():
    pass

def resume():
    pass