import pico2d
import game_framework

import logo_state

pico2d.open_canvas(1920, 1080)
pico2d.hide_cursor()
game_framework.run(logo_state)
pico2d.close_canvas()