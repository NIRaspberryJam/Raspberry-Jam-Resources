import explorerhat as eh
import pygame

pygame.init()

def touch1 (channel, event):
    eh.light.red.on()
    music = Sound("/home/shared/sounds/drum_bass_hard.wav")
    music.play()
    sleep(1)
    eh.light.red.off()


eh.touch.five.pressed(touch1)
