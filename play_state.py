from pico2d import *
from objects import *

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

def draw():
    clear_canvas()
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
    update_canvas()