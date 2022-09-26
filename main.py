def on_button_pressed_a():
    music.set_volume(255)
    basic.show_leds("""
        . . . . .
                . . . # .
                # . # . #
                . # . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # . . .
                # . # . #
                . . . # .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.set_volume(0)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . # . .
                . # . # .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

max7219_matrix.setup(4,
    DigitalPin.P12,
    DigitalPin.P15,
    DigitalPin.P14,
    DigitalPin.P13)
max7219_matrix.for_4_in_1_modules(rotation_direction.COUNTERCLOCKWISE, True)
Musica = 0
Texto = 0
Boton_A = 0
Boton_B = 0
basic.show_leds("""
    . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
""")

def on_forever():
    max7219_matrix.scroll_text("Feliz Cumpleaños Ulises", 0, 1)
basic.forever(on_forever)

def on_forever2():
    if input.button_is_pressed(Button.A):
        for index in range(10):
            pass
    else:
        pass
basic.forever(on_forever2)

def on_forever3():
    if Musica <= 3:
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.HALF))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(494, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.HALF))
        music.play_tone(587, music.beat(BeatFraction.WHOLE))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(784, music.beat(BeatFraction.WHOLE))
        music.play_tone(659, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.HALF))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(494, music.beat(BeatFraction.WHOLE))
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.HALF))
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
        music.play_tone(659, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.HALF))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(587, music.beat(BeatFraction.WHOLE))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.DOUBLE))
    else:
        pass
basic.forever(on_forever3)
