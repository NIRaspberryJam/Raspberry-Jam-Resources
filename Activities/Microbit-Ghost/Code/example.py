from microbit import *
import random

ghost = Image("09990:"
              "99999:"
              "95959:"
              "99999:"
              "09090")

door1 = Image("00900:"
              "09990:"
              "09590:"
              "09590:"
              "09590")

door2 = Image("00900:"
              "09590:"
              "09590:"
              "09590:"
              "09590")

blank = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

all_pics = [ghost, door1, door2]
score = 0

while True:
    if button_a.is_pressed():
        to_show = random.choice(all_pics)
        if to_show == ghost:
            display.show(ghost)
            display.scroll('You lost!')
            display.scroll('Your Score is: ', score)
        elif to_show == door1:
            display.show(door1)
            sleep(1000)
            display.show(blank)
            score = score + 1
        elif to_show == door2:
            display.show(door2)
            sleep(1000)
            display.show(blank)
            score = score + 1