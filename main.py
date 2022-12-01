import pico2d
import logo_state

start_state = logo_state

pico2d.open_canvas(1920, 1080)
pico2d.hide_cursor()

start_state.enter()

while start_state.running:
    start_state.handle_events()
    start_state.update()
    start_state.draw()
    pico2d.delay(0.05)

start_state.exit()

pico2d.close_canvas()
