from signalTeste import *
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import sys
import keyboard

fs = 44100
sd.default.samplerate = fs

tempo = 0.3
amplitude = 1000

signal = Signal()

x, s697 = signal.generateSin(697, amplitude, tempo, fs)
x, s770 = signal.generateSin(770, amplitude, tempo, fs)
x, s852 = signal.generateSin(852, amplitude, tempo, fs)
x, s941 = signal.generateSin(941, amplitude, tempo, fs)
x, s1209 = signal.generateSin(1209, amplitude, tempo, fs)
x, s1336 = signal.generateSin(1336, amplitude, tempo, fs)
x, s1477 = signal.generateSin(1477, amplitude, tempo, fs)

um = s697 + s1209
dois = s697 + s1336
tres = s697 + s1477
quatro = s770 + s1209
cinco = s770 + s1336
seis = s770 + s1477
sete = s852 + s1209
oito = s852 + s1336
nove = s852 + s1477
zero = s941 + s1336

while True:

	if keyboard.is_pressed('1'): 
		sd.play(um)
		sd.wait()
		sd.stop()

	if keyboard.is_pressed('2'): 
		sd.play(dois)
		sd.wait()
		sd.stop()

	if keyboard.is_pressed('3'): 
		sd.play(tres)
		sd.wait()
		sd.stop()

	if keyboard.is_pressed('4'): 
		sd.play(quatro)
		sd.wait()
		sd.stop()

	if keyboard.is_pressed('5'): 
		sd.play(cinco)
		sd.wait()
		sd.stop()
		
	if keyboard.is_pressed('6'): 
		sd.play(seis)
		sd.wait()
		sd.stop()

	if keyboard.is_pressed('7'): 
		sd.play(sete)
		sd.wait()
		sd.stop()

	if keyboard.is_pressed('8'): 
		sd.play(oito)
		sd.wait()
		sd.stop()

	if keyboard.is_pressed('9'): 
		sd.play(nove)
		sd.wait()
		sd.stop()

	if keyboard.is_pressed('0'): 
		sd.play(zero)
		sd.wait()
		sd.stop()

	if keyboard.is_pressed('i'):
		break