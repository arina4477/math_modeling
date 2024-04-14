import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('H.jpg')
fig, ax = plt.subplots()
ax.imshow(img)


t = np.linspace(np.pi-np.pi/8, np.pi/1.8, 100)
x = 400 + 240 * np.cos(t)
y = 800 - 240 * np.sin(t)
ax.plot(x, y, '-', lw=2, color = 'k')


t =  np.linspace(3 * np.pi/2, 2 * np.pi, 200)
x = 360 + 115 * np.cos(t)
y = 348 - 215 * np.sin(t)
ax.plot(x, y, '-', lw=2, color = 'k')


x = [475, 385]
y = [350, 370]
ax.plot(x, y, '-', lw=2, color = 'k')

t =  np.linspace(np.pi/2, 3 * np.pi/2, 200)
x = 380 + 60 * np.cos(t)
y = 320 - 50 * np.sin(t)
ax.plot(x, y, '-', lw=2, color = 'k')

plt.savefig('horse.png')