import numpy as np
from scipy import signal
import simpleaudio as sa

# calculate note frequencies
A_freq = 440
Csh_freq = A_freq * 2 ** (4 / 12)
E_freq = A_freq * 2 ** (7 / 12)

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 1
t = np.linspace(0, T, T * sample_rate, False)
noise = np.random.normal(0, 1, T * 2 *sample_rate)

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)#signal.square(A_freq * t * 2 * np.pi)#
Csh_note = signal.square(Csh_freq * t * 2 * np.pi)
E_note = signal.square(E_freq * t * 2 * np.pi)

#print(A_note[:200], Csh_note[:30], E_note[:30])

# mix audio together
audio = np.zeros((int(sample_rate * T * 2), 2))
n = len(t)
offset = 0
audio[0 + offset: n + offset, 0] += A_note
audio[0 + offset: n + offset, 1] += 0.125 * A_note
offset = n//3
audio[0 + offset: n + offset, 0] += 0.5 * Csh_note
audio[0 + offset: n + offset, 1] += 0.5 * Csh_note
offset = n*2//3
audio[0 + offset: n + offset, 0] += 0.125 * E_note
audio[0 + offset: n + offset, 1] += E_note

audio[:, 0] += noise
audio[:, 1] += noise

# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()

#import numpy as np
#import simpleaudio as sa

## calculate note frequencies
#A_freq = 440
#Csh_freq = A_freq * 2 ** (4 / 12)
#E_freq = A_freq * 2 ** (7 / 12)
#d = A_freq * 2 ** (1)

## get timesteps for each sample, T is note duration in seconds
#sample_rate = 44100
#T = 0.3
#t = np.linspace(0, T, T * sample_rate, False)

## generate sine wave notes
#A_note = np.sin(A_freq * t * 2 * np.pi)
#Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
#E_note = np.sin(E_freq * t * 2 * np.pi)
#dn = np.sin(d * t * 2 * np.pi)

## concatenate notes
#audio = np.hstack((A_note, Csh_note, E_note, dn))
## normalize to 16-bit range
#audio *= 32767 / np.max(np.abs(audio))
## convert to 16-bit data
#audio = audio.astype(np.int16)

## start playback
#play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

## wait for playback to finish before exiting
#play_obj.wait_done()








## Beat tracking example
#from __future__ import print_function
#import librosa

## 1. Get the file path to the included audio example
#filename = librosa.util.example_audio_file()

## 2. Load the audio as a waveform `y`
##    Store the sampling rate as `sr`
#y, sr = librosa.load(filename)

## 3. Run the default beat tracker
#tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

## 4. Convert the frame indices of beat events into timestamps
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)