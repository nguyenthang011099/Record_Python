
import matplotlib.pyplot as plt
import wave
import numpy as np
#read file wav
file = wave.open(r"C:\Users\Dell\PycharmProjects\Word - embedding\xlth2.wav", "rb")

# sound channel
chanels = file.getnchannels()

# Demo frequency
fsample = file.getframerate()

# bit of file
sampwidth= file.getsampwidth()

# frames of sound
nframes = file.getnframes()

#return max frame
frames = file.readframes(-1)


file.close()

frames= np.fromstring(frames,'Int16')

# draw graph
time= np.linspace(0,len(frames)/fsample,num=len(frames))
plt.figure(1)
plt.plot(time,frames)
plt.show()









