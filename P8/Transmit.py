import soundfile as sf
import sounddevice as sd
import numpy as np
from scipy import signal
import math
from signalTeste import *

filename = "leroy.wav"

sound, fs = sf.read(filename)

sd.default.channels = 2
sd.default.samplerate = fs

sd.play(sound, fs)
sd.wait()

def normalize(array):

    max = array.max()

    for i in range(len(array)):
        array[i] = array[i]/max

    return array

sound_norm = normalize(sound)

def filtro(sound_norm, fs):
    nyq_rate = fs/2
    width = 5.0/nyq_rate
    ripple_db = 60.0 #dB
    N , beta = signal.kaiserord(ripple_db, width)
    cutoff_hz = 4000.0
    taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
    yFiltrado = signal.lfilter(taps, 1.0, sound_norm)
    return yFiltrado

sound_filtrado = filtro(sound_norm, fs)

sinal = Signal()

freq = 16000
amplitude = 1
time = len(sound_filtrado)/fs

x, portador = sinal.generateSin(freq, amplitude, time, fs)

modulado = portador * sound_filtrado

sd.play(modulado, fs)
sd.wait()