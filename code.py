threshold = 25
def on_forever():
    if input.temperature() > threshold:
        music.ring_tone(Note.C)
        basic.show_icon(IconNames.SAD)
    else:
        music.stop_all_sounds()
        basic.show_icon(IconNames.HAPPY)
        # basic.clear_screen()
    basic.pause(1000)
basic.forever(on_forever)