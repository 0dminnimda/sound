import pygame
from scipy.io.wavfile import read
import numpy as np
from pynput import keyboard

def on_press(key):
    global but
    try:
        but = key.char
    except AttributeError:
        but = key

def on_release(key):
    pass

m = "Apprehensive_at_Best.mp3"
w = "Apprehensive_at_Best.wav"

n = w

#a = np.array(read(n)[1])
#print(a, a.shape)

pygame.init()

sc = pygame.display.set_mode((400, 300))

pygame.mixer.music.load(n)
pygame.mixer.music.play()

sou = pygame.mixer.Sound(w)

print(np.array(sou.get_raw()).astype(np.int))

but = None

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while 0:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        #elif i.type == pygame.KEYDOWN:
        #    if i.key == pygame.K_1:
        #        sou.pause()
        #        # pygame.mixer.music.stop()
        #    elif i.key == pygame.K_2:
        #        sou.unpause()
        #        # pygame.mixer.music.play()
        #        sou.set_volume(0.5)
        #    elif i.key == pygame.K_3:
        #        sou.unpause()
        #        # pygame.mixer.music.play()
        #        sou.set_volume(1)
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_1:
                pygame.mixer.music.pause()
                # pygame.mixer.music.stop()
            elif i.key == pygame.K_2:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)
            elif i.key == pygame.K_3:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
    pygame.time.delay(60)