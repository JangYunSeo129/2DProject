from pico2d import *
import os
os.chdir('c:\\Users\\user\\Desktop\\tcu\\2-2\\2DGP\\2DProject')

class Fox:
    def __init__(self):
        self.drawaction = 0
        self.frame = 0
        self.image = load_image('player_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        global userinput, x, y
        if userinput == 0:
            self.image.clip_draw(self.frame * 33, 32, 33, 32, x, y, 264, 256)
        else:
            if userinput == 1:
                self.image.clip_draw(self.frame * 33, 32, 33, 32, x, y, 264, 256)
                x = x + 35
                self.drawaction = self.drawaction + 1
                if self.drawaction == 6:
                    self.drawaction = 0
                    userinput = 0
            elif userinput == 2:
                self.image.clip_draw(self.frame * 33, 32, 33, 32, x, y, 264, 256)
                x = x - 35
                self.drawaction = self.drawaction + 1
                if self.drawaction == 6:
                    self.drawaction = 0
                    userinput = 0
            elif userinput == 3:
                if self.drawaction < 5:
                    y = y + 71
                    self.image.clip_draw(0, 0, 33, 32, x, y, 264, 256)
                    self.drawaction = self.drawaction + 1
                elif self.drawaction < 8:
                    self.image.clip_draw(33, 0, 32, 32, x, y, 264, 256)
                    y = y - 33
                    self.drawaction = self.drawaction + 1
                else:
                    self.image.clip_draw(33, 0, 32, 32, x, y, 264, 256)
                    self.drawaction = 0
                    userinput = 0
                    self.frame = 0
            elif userinput == 4:
                self.image.clip_draw(33, 0, 33, 32, x, y, 264, 256)
                y = y - 32
                self.drawaction = self.drawaction + 1
                if self.drawaction == 8:
                    self.drawaction = 0
                    userinput = 0
                    self.frame = 0
            

def handle_events():
    global running, userinput
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
                elif event.key == SDLK_ESCAPE:
                    running == False

open_canvas(1920, 1080)
x, y = 400, 300
userinput = 0
drawaction = 0
fox = Fox()
running = True
        
while running:
    handle_events()

    fox.update()

    clear_canvas()
    fox.draw()
    update_canvas()

    delay(0.06)
