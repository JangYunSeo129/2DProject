from pico2d import *
from objects import Fox
from objects import Heart
from objects import Background
from objects import Platform
from objects import Cherry
from objects import Gem
from objects import Eagle
from objects import Frog
from objects import Boss
import game_framework
import pause_state

fox = None
heart = None
background = None
under_platform = None
over_platform = None
cherry = None
gem = None
eagle = None
frog = None
boss1 = None
running = None

def enter():
    global fox, heart, background, under_platform, over_platform, cherry, gem, eagle, frog, boss1, running
    
    fox = Fox()
    heart = Heart()
    background = Background()
    under_platform = Platform()
    over_platform = Platform()
    cherry = Cherry()
    gem = Gem()
    eagle = Eagle()
    frog = Frog()
    boss1 = Boss()
    running = True

def exit():
    global fox, heart, background, under_platform, over_platform, cherry, gem, eagle, frog, boss1
    del fox
    del heart
    del background
    del under_platform
    del over_platform
    del cherry
    del gem
    del eagle
    del frog
    del boss1

def update():
    background.update()
    cherry.update()
    gem.update()
    eagle.update()
    frog.update()
    boss1.update()
    fox.update()
    delay(0.05)

def draw_world():
    background.draw()
    under_platform.draw(1)
    over_platform.draw(2)
    heart.draw()
    fox.draw()
    cherry.draw()
    eagle.draw()
    frog.draw()
    boss1.draw()
    gem.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
        else:
            fox.handle_event(event)
        delay(0.01)

def pause():
    pass

def resume():
    pass
        