from pico2d import *
import game_framework

# fill here

def enter():
    # fill here
    pass

def exit():
    # fill here
    pass

def update():
    # fill here
    pass

def draw():
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case SDLK_ESCAPE:
                    game_framework.pop_state()