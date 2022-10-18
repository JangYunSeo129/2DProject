from math import ceil
from re import S
from pico2d import *
import os
import random
os.chdir('c:\\Users\\user\\Desktop\\tcu\\2-2\\2DGP\\2DProject')

class Fox:
    def __init__(self):
        self.drawaction = 0
        self.row, self.col = 1, 1
        self.frame = 0
        self.image = load_image('player_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        global userinput, foxx, foxy
        if userinput == 0:
            self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
        else:
            if userinput == 1:
                if self.row == 4:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    userinput = 0
                else:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    foxx = foxx + 35
                    self.drawaction = self.drawaction + 1
                    if self.drawaction == 6:
                        self.row = self.row + 1
                        self.drawaction = 0
                        userinput = 0
            elif userinput == 2:
                if self.row == 1:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    userinput = 0
                else:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    foxx = foxx - 35
                    self.drawaction = self.drawaction + 1
                    if self.drawaction == 6:
                        self.row = self.row - 1
                        self.drawaction = 0
                        userinput = 0
            elif userinput == 3:
                if self.col == 3:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    userinput = 0
                else:
                    if self.drawaction < 5:
                        foxy = foxy + 71
                        self.image.clip_draw(0, 0, 33, 32, foxx, foxy, 264, 256)
                        self.drawaction = self.drawaction + 1
                    elif self.drawaction < 8:
                        self.image.clip_draw(33, 0, 32, 32, foxx, foxy, 264, 256)
                        foxy = foxy - 33
                        self.drawaction = self.drawaction + 1
                    else:
                        self.image.clip_draw(33, 0, 32, 32, foxx, foxy, 264, 256)
                        self.col = self.col + 1
                        self.drawaction = 0
                        userinput = 0
                        self.frame = 0
            elif userinput == 4:
                if self.col == 1:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    userinput = 0
                else:
                    self.image.clip_draw(33, 0, 33, 32, foxx, foxy, 264, 256)
                    foxy = foxy - 32
                    self.drawaction = self.drawaction + 1
                    if self.drawaction == 8:
                        self.col = self.col - 1
                        self.drawaction = 0
                        userinput = 0
                        self.frame = 0
            
class Background:
    def __init__(self):
        self.frame = 0
        self.image = load_image('background.png')

    def update(self):
        self.frame = (self.frame + 1) % 77

    def draw(self):
        self.image.clip_draw(self.frame * 5, 0, 240, 240, 960, 540, 1920, 1080)

class Cherry:
    def __init__(self):
        self.x, self.y = 0, 0
        self.spawn = 0
        self.frame = 0
        self.image = load_image('item1_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 7

    def draw(self):
        global spawnmob
        if spawnmob == 4:
            self.spawn = 1
            spawnmob = 0
            randx, randy = random.randint(1, 4), random.randint(1, 3)
            if self.spawn == 1:
                if randx ==  1:
                    self.x = 400
                elif randx == 2:
                    self.x = 610
                elif randx == 3:
                    self.x = 820
                elif randx == 4:
                    self.x = 1030
                if randy ==  1:
                    self.y = 300
                elif randy == 2:
                    self.y = 556
                elif randy == 3:
                    self.y = 812
        if self.spawn == 1:
            self.image.clip_draw(self.frame * 21, 0, 21, 21, self.x, self.y, 168, 168)

class Gem:
    def __init__(self):
        self.x, self.y = 400, 300
        self.spawn = 0
        self.frame = 0
        self.image = load_image('item2_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 5

    def draw(self):
        global spawnmob
        if spawnmob == 3:
            self.spawn = 1
            spawnmob = 0
            randx, randy = random.randint(1, 4), random.randint(1, 3)
            if self.spawn == 1:
                if randx ==  1:
                    self.x = 400
                elif randx == 2:
                    self.x = 610
                elif randx == 3:
                    self.x = 820
                elif randx == 4:
                    self.x = 1030
                if randy ==  1:
                    self.y = 300
                elif randy == 2:
                    self.y = 556
                elif randy == 3:
                    self.y = 812
        if self.spawn == 1:
            self.image.clip_draw(self.frame * 15, 0, 15, 13, self.x, self.y, 120, 104)

class Frog:
    def __init__(self):
        self.x, self.y = 2100, 262 
        self.spawn = 0
        self.frame = 0
        self.image = load_image('enemy1_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 12

    def draw(self):
        global spawnmob
        if spawnmob == 1:   #등장 조건 바꿔야함
            self.spawn = 1
            spawnmob = 0
        if self.spawn == 1:
            # if rand 1,2 1뛰기 2안뛰기 FRAME //3도 바꿔줄수있으면 바꾸자
            self.image.clip_draw(((self.frame // 3)* 35) + 70, 32, 35, 32, self.x, self.y, 264, 256)
            self.x = self.x - 40
            if self.x < 0:
                self.x = 2100
                self.spawn = 0

class Eagle:
    def __init__(self):
        self.x, self.y = 2100, 812
        self.spawn = 0
        self.frame = 0
        self.image = load_image('enemy2_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        global spawnmob
        if spawnmob == 2:   #등장 조건 바꿔야함
            self.spawn = 1
            spawnmob = 0
        if self.spawn == 1:
            self.image.clip_draw(self.frame * 40, 0, 40, 41, self.x, self.y, 264, 256)
            self.x = self.x - 40
            if self.x < 0:
                self.x = 2100
                self.spawn = 0

def handle_events():
    global running, userinput, spawnmob
    global x, y
    events = get_events()
    for event in events:
        if userinput == 0:
            if event.type == SDL_QUIT:
                running = False  
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    userinput = 1
                elif event.key == SDLK_LEFT:
                    userinput = 2
                elif event.key == SDLK_UP:
                    userinput = 3
                elif event.key == SDLK_DOWN:
                    userinput = 4
                elif event.key == SDLK_q:
                    spawnmob = 1
                elif event.key == SDLK_w:
                    spawnmob = 2
                elif event.key == SDLK_e:
                    spawnmob = 3
                elif event.key == SDLK_r:
                    spawnmob = 4
                elif event.key == SDLK_ESCAPE:
                    running = False

open_canvas(1920, 1080)
foxx, foxy = 400, 300
userinput = 0
spawnmob = 0
drawaction = 0
fox = Fox()
background = Background()
cherry = Cherry()
gem = Gem()
eagle = Eagle()
frog = Frog()
running = True
        
while running:
    handle_events()

    background.update()
    cherry.update()
    gem.update()
    eagle.update()
    frog.update()
    fox.update()

    clear_canvas()
    background.draw()
    cherry.draw()
    gem.draw()
    eagle.draw()
    frog.draw()
    fox.draw()
    update_canvas()

    delay(0.06)
