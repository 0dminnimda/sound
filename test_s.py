import numpy as np
import simpleaudio as sa
import pydub
#from pydub import AudioSegment
from scipy.io.wavfile import read, write
import time
from pynput import keyboard
from audio2numpy import open_audio

#import os
#import sys
#list = os.listdir(sys.path[0])
#print(list)
#p = list[1]#sys.path[0]+#"\Apprehensive_at_Best.mp3" #"C:\Python\projects\sound\Apprehensive_at_Best.mp3"
#print(p)

m = "Apprehensive_at_Best.mp3"
w = "Apprehensive_at_Best.wav"

n = w

#aaa = pydub.AudioSegment.from_mp3(m)

#signal, sampling_rate = open_audio(n)
#wave_obj = sa.WaveObject.from_wave_file

a = np.array(read(n)[1])#.astype(np.float64)
T = read(n)[0]
print(a, a.shape)
v = a.shape[0]# * 1 * T

noise = np.random.normal(0, 2000, v).astype(np.int16)

a[0:v, 0] += noise
a[0:v, 1] += noise

a *= 32767 // np.max(a)

#a = a.astype(np.int16)
#write

#frequency = 1000  # Our played note will be 440 Hz
#seconds = 1  # Note duration of 3 seconds

## Generate array with seconds*sample_rate steps, ranging between 0 and seconds
#t = np.linspace(0, seconds, seconds * fs, False)

## Generate a 440 Hz sine wave
#note = np.sin(frequency * t * 1 * np.pi)

## Ensure that highest value is in 16-bit range
#audio = note * (2**15 - 1) / np.max(np.abs(note))

## Convert to 16-bit data
#audio = audio.astype(np.int16)
#print(audio)



# Start playback
plo = sa.play_buffer(a, 2, 2, T)

plo.wait_done()

