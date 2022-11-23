from math import ceil
from re import S
from pico2d import *
import os
import random
os.chdir('c:\\Users\\user\\Desktop\\tcu\\2-2\\2DGP\\2DProject')


class Fox:
    def __init__(self):
        self.drawaction = 0
        self.frame = 0
        self.x, self.y = 0, 0
        self.image = load_image('player_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        global foxrow, foxcol
        global userinput, foxx, foxy
        if foxhealth == 0:
            if self.x == 0:
                self.x, self.y = foxx, foxy
            foxx, foxy = -10000, -10000
            self.image.clip_draw(66, 0, 33, 32, self.x, self.y, 264, 256)
        
        if userinput == 0:
            self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
        else:
            if userinput == 1:
                if foxrow == 4:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    userinput = 0
                else:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    foxx = foxx + 35
                    self.drawaction = self.drawaction + 1
                    if self.drawaction == 6:
                        foxrow = foxrow + 1
                        self.drawaction = 0
                        userinput = 0
            elif userinput == 2:
                if foxrow == 1:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    userinput = 0
                else:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    foxx = foxx - 35
                    self.drawaction = self.drawaction + 1
                    if self.drawaction == 6:
                        foxrow = foxrow - 1
                        self.drawaction = 0
                        userinput = 0
            elif userinput == 3:
                if foxcol == 3:
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
                        foxcol = foxcol + 1
                        self.drawaction = 0
                        userinput = 0
                        self.frame = 0
            elif userinput == 4:
                if foxcol == 1:
                    self.image.clip_draw(self.frame * 33, 32, 33, 32, foxx, foxy, 264, 256)
                    userinput = 0
                else:
                    self.image.clip_draw(33, 0, 33, 32, foxx, foxy, 264, 256)
                    foxy = foxy - 32
                    self.drawaction = self.drawaction + 1
                    if self.drawaction == 8:
                        foxcol = foxcol - 1
                        self.drawaction = 0
                        userinput = 0
                        self.frame = 0


class Heart():
    def __init__(self):
        self.image = load_image('ui_heart.png')

    def draw(self):
        if foxhealth == 3:
            self.image.clip_draw(0, 16, 16, 16, 350, 1000, 240, 240)
        else:
            self.image.clip_draw(16, 16, 16, 16, 350, 1000, 240, 240)
        if foxhealth >= 2:
            self.image.clip_draw(0, 16, 16, 16, 220, 1000, 240, 240)
        else:
            self.image.clip_draw(16, 16, 16, 16, 220, 1000, 240, 240)
        if foxhealth == 0:
            self.image.clip_draw(16, 16, 16, 16, 90, 1000, 240, 240)
        else:
            self.image.clip_draw(0, 16, 16, 16, 90, 1000, 240, 240)

class Platform:
    def __init__(self):
        self.image = load_image('platform.png')
    
    def draw(self, x):
        if x == 1:
            self.image.clip_draw(0, 0, 128, 16, 705, 400, 840, 64)
        elif x == 2:
            self.image.clip_draw(0, 0, 128, 16, 705, 655, 840, 64)

class Background:
    def __init__(self):
        self.frame = 0
        self.image = load_image('backplus.png')

    def update(self):
        if foxhealth > 0:
            self.frame = (self.frame + 1) % 77

    def draw(self):
        self.image.clip_draw(self.frame * 5, 0, 240, 240, 960, 540, 1920, 1080)

class Cherry:
    def __init__(self):
        self.x, self.y = -200, -200
        self.row, self.col = 0, 0
        self.frame = 0
        self.spawn = 0
        self.image = load_image('item1_sheet.png')
        self.effect = load_image('item_effect.png')
        self.effectdraw, self.ex, self.ey = 0, 0, 0

    def update(self):
        self.frame = (self.frame + 1) % 7

    def draw(self):
        global userscore, foxhealth
        self.spawn += 1
        if self.spawn == 400:
            self.row, self.col = random.randint(1, 4), random.randint(1, 3)
            self.spawn = 0
        if foxrow == self.row and foxcol == self.col:
            if foxhealth < 3:
                foxhealth += 1
            self.ex, self.ey = self.x, self.y
            self.row, self.col = 0, 0
            self.x, self.y = -200, -200
            userscore += 1
            self.effectdraw = 0
            print(userscore)

        if self.effectdraw < 8:
            self.effect.clip_draw((self.effectdraw//2) * 32, 0, 32, 32, self.ex, self.ey, 192, 192)
            self.effectdraw += 1   

        if self.row ==  1:
                self.x = 400
        elif self.row == 2:
                self.x = 610
        elif self.row == 3:
                self.x = 820
        elif self.row == 4:
                self.x = 1030
        if self.col ==  1:
                self.y = 280
        elif self.col == 2:
                self.y = 536
        elif self.col == 3:
                self.y = 792
                
        self.image.clip_draw(self.frame * 21, 0, 21, 21, self.x, self.y, 147, 147)

class Gem:
    def __init__(self):
        self.x, self.y = -200, -200
        self.row, self.col = random.randint(1, 4), random.randint(1, 3)
        self.frame = 0
        self.image = load_image('item2_sheet.png')
        self.effect = load_image('item_effect.png')
        self.effectdraw, self.ex, self.ey = 0, 0, 0

    def update(self):
        self.frame = (self.frame + 1) % 5

    def draw(self):
        global userscore
        if foxrow == self.row and foxcol == self.col:
            self.ex, self.ey = self.x, self.y
            self.row, self.col = random.randint(1, 4), random.randint(1, 3)
            userscore += 1
            self.effectdraw = 0
            print(userscore)

        if self.effectdraw < 8:
            self.effect.clip_draw((self.effectdraw//2) * 32, 0, 32, 32, self.ex, self.ey, 192, 192)
            self.effectdraw += 1   

        if self.row ==  1:
                self.x = 400
        elif self.row == 2:
                self.x = 610
        elif self.row == 3:
                self.x = 820
        elif self.row == 4:
                self.x = 1030
        if self.col ==  1:
                self.y = 280
        elif self.col == 2:
                self.y = 536
        elif self.col == 3:
                self.y = 792
                
        self.image.clip_draw(self.frame * 15, 0, 15, 13, self.x, self.y, 120, 104)

class Frog:
    def __init__(self):
        self.x, self.y = 2100, 262 
        self.spawn = 0
        self.frame = 0
        self.image = load_image('enemy1_sheet.png')
        self.effect = load_image('enemy_effect.png')
        self.effectdraw, self.ex, self.ey = 0, 0, 0

    def update(self):
        self.frame = (self.frame + 1) % 12

    def draw(self):
        global spawnmob, foxhealth
        if spawnmob == 1:   #등장 조건 바꿔야함
            self.spawn = 1
            spawnmob = 0
        if self.spawn == 1:
            # if rand 1,2 1뛰기 2안뛰기 FRAME //3도 바꿔줄수있으면 바꾸자
            self.image.clip_draw(((self.frame // 3)* 35) + 70, 32, 35, 32, self.x, self.y, 264, 256)
            self.x = self.x - 30
            if self.x < 0:
                self.x = 2100
                self.spawn = 0

        if foxy > self.y + 128:
            pass
        else:
            if foxx - self.x < 0:
                if self.x - foxx < 132:
                    foxhealth -= 1
                    self.ex, self.ey = self.x, self.y
                    self.effectdraw = 0
                    self.x = 2100
                    self.spawn = 0
            elif foxx - self.x < 132:
                foxhealth -= 1
                self.ex, self.ey = self.x, self.y
                self.effectdraw = 0
                self.x = 2100
                self.spawn = 0
        if self.effectdraw < 12:
            self.effect.clip_draw((self.effectdraw//2) * 40, 0, 40, 41, self.ex, self.ey, 192, 192)
            self.effectdraw += 1

class Eagle:
    def __init__(self):
        self.x, self.y = 2100, 812
        self.spawn = 0
        self.frame = 0
        self.image = load_image('enemy2_sheet.png')
        self.effect = load_image('enemy_effect.png')
        self.effectdraw, self.ex, self.ey = 0, 0, 0

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        global spawnmob, foxhealth
        if spawnmob == 2:   #등장 조건 바꿔야함
            self.spawn = 1
            spawnmob = 0
        if self.spawn == 1:
            self.image.clip_draw(self.frame * 40, 0, 40, 41, self.x, self.y, 264, 256)
            self.x = self.x - 45
            if self.x < 0:
                self.x = 2100
                self.spawn = 0

        if foxy < self.y - 132:
            pass
        else:
            if foxx - self.x < 0:
                if self.x - foxx < 132:
                    foxhealth -= 1
                    self.ex, self.ey = self.x, self.y
                    self.effectdraw = 0
                    self.x = 2100
                    self.spawn = 0
            elif foxx - self.x < 132:
                foxhealth -= 1
                self.ex, self.ey = self.x, self.y
                self.effectdraw = 0
                self.x = 2100
                self.spawn = 0
        if self.effectdraw < 12:
            self.effect.clip_draw((self.effectdraw//2) * 40, 0, 40, 41, self.ex, self.ey, 192, 192)
            self.effectdraw += 1

class Boss:
    def __init__(self):
        self.spawn = 0
        self.frame = 0
        self.x, self.y = 2400, 330
        self.image = load_image('enemy1_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 12

    def draw(self):
        global spawnmob
        if spawnmob == 3:   #등장 조건 바꿔야함
            self.spawn = 1
            spawnmob = 0
        if self.spawn == 1:
            self.image.clip_composite_draw((self.frame//2 * 36), 0, 36, 32, 0, 'h', self.x, self.y, 720, 640)
            if self.x > 1550:
                self.x = self.x - 25
            

def handle_events():
    global running, userinput, spawnmob
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
                    print(running)

foxx, foxy = 400, 300
foxrow, foxcol = 1, 1
foxhealth = 3                 #체력관련사용변수 (frog, eagle에서사용중)
userinput = 0            
spawnmob = 0  
userscore = 0              #점수관련사용변수 (gem에서사용중)