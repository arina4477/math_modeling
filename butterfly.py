import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('бабочака.jpg')
fig, ax = plt.subplots()
ax.imshow(img)


t0 = np.linspace(0-np.pi/14, -np.pi/2-np.pi/30, 100)
x0 = 240 + 240 * np.cos(t0)
y0 = 290 - 180 * np.sin(t0)
ax.plot(x0, y0, '-', lw=2, color = 'w')

t1 =  np.linspace(0, np.pi/2 + np.pi/44, 200)
x1 = 70 + 140 * np.cos(t1)
y1 = 470 -110 * np.sin(t1)
ax.plot(x1, y1, '-', lw=2, color = 'w')

x = np.append(x0, x1)
y = np.append(y0, y1)


t2 =  np.linspace( np.pi, np.pi/2, 200)
x2 = 260 + 200 * np.cos(t2)
y2 = 360 - 80 * np.sin(t2)
ax.plot(x2, y2, '-', lw=2, color = 'w')


x = np.append(x, x2)
y = np.append(y, y2)

t3 =  np.linspace(np.pi, 3 * np.pi/2 + np.pi/30, 200)
x3 = 265 + 22 * np.cos(t3)
y3 = 215 - 65 * np.sin(t3)
ax.plot(x3, y3, '-', lw=2, color = 'w')

x = np.append(x, x3)
y = np.append(y, y3)

t4 =  np.linspace (np.pi/2, np.pi,200)
x4 = 310 + 67 * np.cos(t4)
y4 = 211 - 11 * np.sin(t4)
ax.plot(x4, y4, '-', lw=2, color = 'w')

x = np.append(x, x4)
y = np.append(y, y4)

t5 =  np.linspace(3 * np.pi/2, np.pi, 200)
x5 = 310 + 17 * np.cos(t5)
y5= 105 - 93 * np.sin(t5)
ax.plot(x5, y5, '-', lw=2, color = 'w')

x = np.append(x, x5)
y = np.append(y, y5)

t6 =  np.linspace(np.pi/2 + np.pi/75, 0 , 200)
x6 = 300.05 + 189 * np.cos(t6)
y6 = 250 - 150 * np.sin(t6)
ax.plot(x6, y6, '-', lw=2, color = 'w')

x = np.append(x, x6)
y = np.append(y, y6)

plt.savefig('butterfly.png')