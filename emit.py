from signalTeste import *
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import sys

fs = 44100
sd.default.samplerate = fs

tempo = 1
amplitude = 1000

signal = Signal()

x, s1209 = signal.generateSin(1209,amplitude,tempo,fs)
x, s697 = signal.generateSin(697,amplitude,tempo,fs)

um = s1209 + s697

x, array = signal.calcFFT(um, fs)
sd.play(um)
sd.stop()