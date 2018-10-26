import soundfile as sf
import sounddevice as sd
from signalTeste import *
import matplotlib.pyplot as plt
import numpy as np
import math

fs = 44100
channel = 2
sd.default.samplerate = fs
sd.default.channels = channel

signal = Signal()

recording = True

time = 1
amplitude = 1
freq = 16000

x, portador = signal.generateSin(freq, amplitude, time, fs)

while recording:

    print("gravando")

    myrecording = sd.rec(int(time * fs))
    sd.wait()


    myrecording = [i[0] for i in myrecording]

    sd.play(myrecording)
    sd.wait()

    signal.plotFFT(myrecording, fs)
    plt.show()

    
    
