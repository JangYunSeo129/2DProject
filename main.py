import pico2d
import play_state

pico2d.open_canvas(1920, 1080)
pico2d.hide_cursor()

play_state.enter()

while play_state.running:
    play_state.handle_events()
    play_state.update()
    play_state.draw()
    pico2d.delay(0.05)

play_state.exit()

pico2d.close_canvas()
