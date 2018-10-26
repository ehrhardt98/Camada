import soundfile as sf
import sounddevice as sd
from signalTeste import *
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal

fs = 44100
channel = 2
sd.default.samplerate = fs
sd.default.channels = channel

sinal = Signal()

time = 5
amplitude = 1
freq = 16000

x, portadora = sinal.generateSin(freq, amplitude, time, fs)

print("gravando")

myrecording = sd.rec(int(time * fs))
sd.wait()

print("reproduzindo")

myrecording = [i[0] for i in myrecording]

sd.play(myrecording)
sd.wait()

def filtro(sound, fs):
    nyq_rate = fs/2
    width = 5.0/nyq_rate
    ripple_db = 60.0 #dB
    N , beta = signal.kaiserord(ripple_db, width)
    cutoff_hz = 4000.0
    taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
    yFiltrado = signal.lfilter(taps, 1.0, sound)
    return yFiltrado


x = []
for i in range(len(myrecording)):
    x.append(i)

recebido = portadora * myrecording

demodulado = filtro(recebido, fs)

print("Myrecording - Tempo")
plt.plot(x, myrecording)
plt.show()

print("Myrecording - FS")
sinal.plotFFT(myrecording, fs)
plt.show()

print("Demodulado - Tempo")
plt.plot(x, demodulado)
plt.show()

print("Demodulado - FS")
sinal.plotFFT(demodulado, fs)
plt.show()


def normalize(array):

    max = array.max()

    for i in range(len(array)):
        array[i] = array[i]/max

    return array

demodulado_norm = normalize(demodulado)

sd.play(demodulado_norm)
sd.wait()