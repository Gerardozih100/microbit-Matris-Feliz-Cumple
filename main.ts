input.onButtonPressed(Button.A, function () {
    music.setVolume(255)
    basic.showLeds(`
        . . . . .
        . . . # .
        # . # . #
        . # . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # . . .
        # . # . #
        . . . # .
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function () {
    music.setVolume(0)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        `)
})
max7219_matrix.setup(
4,
DigitalPin.P12,
DigitalPin.P15,
DigitalPin.P14,
DigitalPin.P13
)
max7219_matrix.for_4_in_1_modules(
rotation_direction.counterclockwise,
true
)
let Musica = 0
let Texto = 0
let Boton_A = 0
let Boton_B = 0
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
basic.forever(function () {
    max7219_matrix.scrollText(
    "Feliz Cumpleaños Ulises",
    0,
    1
    )
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        for (let index = 0; index < 10; index++) {
        	
        }
    } else {
    	
    }
})
basic.forever(function () {
    if (Musica <= 3) {
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Half))
        music.playTone(523, music.beat(BeatFraction.Whole))
        music.playTone(494, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Half))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Half))
        music.playTone(587, music.beat(BeatFraction.Whole))
        music.playTone(523, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Half))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(784, music.beat(BeatFraction.Whole))
        music.playTone(659, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Half))
        music.playTone(523, music.beat(BeatFraction.Whole))
        music.playTone(494, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Half))
        music.playTone(698, music.beat(BeatFraction.Whole))
        music.playTone(698, music.beat(BeatFraction.Whole))
        music.playTone(659, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Half))
        music.playTone(523, music.beat(BeatFraction.Whole))
        music.playTone(587, music.beat(BeatFraction.Whole))
        music.playTone(523, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Double))
    } else {
    	
    }
})
