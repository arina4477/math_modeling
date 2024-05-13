import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
R = 1

def circle(a, b, r):
    t = 100
    x, y = [0] * t, [0] * t
    for i, frame in enumerate(np.linspace(0, 2 * np.pi, t)):
        x[i] = a + r * np.cos(frame)
        y[i] = b + r * np.sin(frame)
    return x, y


Frames = np.linspace(0, 4 * np.pi, 100)
x1 = R * (Frames - np.sin(Frames))
y1 = R * (1 - np.cos(Frames))
cycloid_c = R * Frames
fig = plt.figure()

lns = []
for i in range(len(Frames)):
    x, y = circle(cycloid_c[i], R, R)
    k, = plt.plot(x, y, 'g', lw=2)
    c,= plt.plot(x1[:i + 1], y1[:i + 1], 'r', lw=2)
    t, = plt.plot(x1[i], y1[i], 'bo')
    r, = plt.plot([cycloid_c[i], x1[i]], [R, y1[i]], 'y', lw=2)
    
    lns.append([k, c, t, r])
plt.xlim(0, 15)
plt.ylim(0, 3)
plt.xlabel('x')
plt.ylabel('y')
# plt.axis('equal')
plt.gca().set_aspect('equal')
ani = animation.ArtistAnimation(fig, 
                                lns, 
                                interval=50
                                )
ani.save('homework.gif')
