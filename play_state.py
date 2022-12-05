from pico2d import *
from objects import Fox
from objects import Heart
from objects import Background
from objects import Platform
from objects import Cherry
from objects import Gem
from objects import Eagle
from objects import Frog
from objects import Rock
from objects import Boss
import game_framework
import pause_state
import ending_state

fox = None
heart = None
background = None
under_platform = None
over_platform = None
cherry = None
gem = None
eagle = None
frog = None
rock = None
boss1 = None
diecountdown = 20
bgm = None
running = None

def enter():
    global fox, heart, background, under_platform, over_platform, cherry, gem, eagle, frog, rock, boss1, running, bgm
    
    fox = Fox()
    heart = Heart()
    background = Background()
    under_platform = Platform()
    over_platform = Platform()
    cherry = Cherry()
    gem = Gem()
    eagle = Eagle()
    frog = Frog()
    rock = Rock()
    boss1 = Boss()
    bgm = load_music('main.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()
    running = True

def exit():
    global fox, heart, background, under_platform, over_platform, cherry, gem, eagle, frog, rock, boss1 , bgm
    del fox
    del heart
    del background
    del under_platform
    del over_platform
    del cherry
    del gem
    del eagle
    del frog
    del rock
    del boss1
    del bgm

def update():
    global diecountdown
    background.update()
    cherry.update()
    gem.update()
    eagle.update()
    frog.update()
    rock.update()
    boss1.update()
    fox.update()
    if fox.health() == 0:
        diecountdown -= 1
        if diecountdown == 0:
            game_framework.change_state(ending_state)
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
    rock.draw()
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
        