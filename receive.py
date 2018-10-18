from signalTeste import *
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import peakutils
import keyboard

fs = 44100
duration = 1
sd.default.samplerate = fs

signal = Signal()

recording = True

while recording:

	myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)

	signals = []

	for i in myrecording:
		signals.append(i[0])

	x, y = signal.plotFFT(signals, fs)

	indexes = peakutils.indexes(y, thres=0.3, min_dist=100)
	if indexes != []:
		print(indexes)

	if keyboard.is_pressed('i'):
		recording = False