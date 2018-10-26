import soundfile as sf
import sounddevice as sd
import numpy as np
from scipy import signal
import math
from signalTeste import *

filename = "terror.wav"

sinal = Signal()

#sound, fs = sf.read(filename)
fs = 44100
time0 = 3
sd.default.channels = 2
sd.default.samplerate = fs

print("Gravando")
sound = sd.rec(int(time0*fs))
sd.wait()
print("Terminou de Gravar")

sound = [i[0] for i in sound]

x = []
for i in range(len(sound)):
    x.append(i)

#Plot sound
print("Sound - Tempo")
plt.plot(x, sound)
plt.show()

print("Sound - FS")
sinal.plotFFT(sound, fs)
plt.show()

print("Sound Reproducao")
sd.play(sound, fs)
sd.wait()

def normalize(array):

    max = np.amax(array)

    for i in range(len(array)):
        array[i] = array[i]/max

    return array

sound_norm = normalize(sound)

#Plot sound_norm
print("Sound_Norm - Tempo")
plt.plot(x, sound_norm)
plt.show()

print("Sound_Norm - FS")
sinal.plotFFT(sound_norm, fs)
plt.show()

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

#Plot sound_filtrado
print("Sound_Filtrado - Tempo")
plt.plot(x, sound_filtrado)
plt.show()

print("Sound_Filtrado - FS")
sinal.plotFFT(sound_filtrado, fs)
plt.show()

freq = 16000
amplitude = 1
time = len(sound_filtrado)/fs

x1, portador = sinal.generateSin(freq, amplitude, time, fs)

sound_modulado = portador * sound_filtrado

#Plot sound_modulado
print("Sound_Modulado - Tempo")
plt.plot(x, sound_modulado)
plt.show()

print("Sound_Modulado - FS")
sinal.plotFFT(sound_modulado, fs)
plt.show()

print("Sound_Modulado - Reproducao")
sd.play(sound_modulado, fs)
sd.wait()