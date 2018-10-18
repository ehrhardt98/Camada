from signalTeste import *
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import peakutils
import keyboard
from peakutils.plot import plot as pplot

fs = 44100
duration = 1
channel = 2
sd.default.samplerate = fs
sd.default.channels = channel

signal = Signal()

recording = True

while recording:

	myrecording = sd.rec(int(duration * fs))

	signals = []

	for i in myrecording:
		signals.append(i[0])

	x, y = signal.calcFFT(signals, fs)

	indexes = peakutils.indexes(y, thres=0.6, min_dist=100)

	pplot(x,y,indexes)

	if indexes != []:
		print(indexes)

	if keyboard.is_pressed('i'):
		recording = False