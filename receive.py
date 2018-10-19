from signalTeste import *
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import peakutils
import keyboard
import heapq
import math

fs = 44100
tempo = 1
amplitude = 1000
channel = 2
sd.default.samplerate = fs
sd.default.channels = channel

signal = Signal()

x1, s697 = signal.generateSin(697, amplitude, tempo, fs)
x1, s770 = signal.generateSin(770, amplitude, tempo, fs)
x1, s852 = signal.generateSin(852, amplitude, tempo, fs)
x1, s941 = signal.generateSin(941, amplitude, tempo, fs)
x1, s1209 = signal.generateSin(1209, amplitude, tempo, fs)
x1, s1336 = signal.generateSin(1336, amplitude, tempo, fs)
x1, s1477 = signal.generateSin(1477, amplitude, tempo, fs)

recording = True

while recording:

	myrecording = sd.rec(int(tempo * fs))
	sd.wait()

	signals = []

	for i in myrecording:
		signals.append(i[0])

	x, y = signal.calcFFT(signals, fs)

	#y = sorted(y)
	#indexes = [y[len(y)-2],y[len(y)-1]]

	#signal.plotFFT(signals, fs)
	#plt.show()

	indexes = peakutils.indexes(np.abs(y), thres=0.1, min_dist=100)

	#indexes = heapq.nlargest(2, indexes)

	print(indexes)

	index_check = []

	for i in indexes:
		if math.isclose(i, 697,rel_tol=0.02):
			index_check.append(697)

		if math.isclose(i, 770,rel_tol=0.02):
			index_check.append(770)

		if math.isclose(i, 852,rel_tol=0.02):
			index_check.append(852)

		if math.isclose(i, 1209,rel_tol=0.02):
			index_check.append(1209)

		if math.isclose(i, 1336,rel_tol=0.02):
			index_check.append(1336)

		if math.isclose(i, 1477,rel_tol=0.02):
			index_check.append(1477)

		if math.isclose(i, 941,rel_tol=0.02):
			index_check.append(941)

	if 697 in index_check and 1209 in index_check:
		print("1")
		signal.plotFFT(signals, fs)
		plt.show()
		plt.plot(x1, s697)
		plt.plot(x1, s1209)
		plt.show()

	if 697 in index_check and 1336 in index_check:
		print("2")
		signal.plotFFT(signals, fs)
		plt.show()
		plt.plot(x1, s697)
		plt.plot(x1, s1336)
		plt.show()

	if 697 in index_check and 1477 in index_check:
		print("3")
		signal.plotFFT(signals, fs)
		plt.show()
		plt.plot(x1, s697)
		plt.plot(x1, s1477)
		plt.show()

	if 770 in index_check and 1209 in index_check:
		print("4")
		signal.plotFFT(signals, fs)
		plt.plot(x1, s770)
		plt.plot(x1, s1209)
		plt.show()

	if 770 in index_check and 1336 in index_check:
		print("5")
		signal.plotFFT(signals, fs)
		plt.show()
		plt.plot(x1, s770)
		plt.plot(x1, s1336)
		plt.show()

	if 770 in index_check and 1477 in index_check:
		print("6")
		signal.plotFFT(signals, fs)
		plt.show()
		plt.plot(x1, s770)
		plt.plot(x1, s1477)
		plt.show()

	if 852 in index_check and 1209 in index_check:
		print("7")
		signal.plotFFT(signals, fs)
		plt.show()
		plt.plot(x1, s852)
		plt.plot(x1, s1209)
		plt.show()

	if 852 in index_check and 1336 in index_check:
		print("8")
		signal.plotFFT(signals, fs)
		plt.show()
		plt.plot(x1, s852)
		plt.plot(x1, s1336)
		plt.show()

	if 852 in index_check and 1477 in index_check:
		print("9")
		signal.plotFFT(signals, fs)
		plt.show()
		plt.plot(x1, s852)
		plt.plot(x1, s1477)
		plt.show()

	if 941 in index_check and 1336 in index_check:
		print("0")
		signal.plotFFT(signals, fs)
		plt.show()
		plt.plot(x1, s941)
		plt.plot(x1, s1336)
		plt.show()