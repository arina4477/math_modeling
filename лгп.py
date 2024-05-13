import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

xdata, ydata = [], []


x = []
y = []
dt = 0.01

theta = 0

while theta < 2*np.pi:
    Ox = 8 * theta / (2*np.pi)
    Oy = 4

    # Позиция точки на окружности
    Px = Ox + 4 * np.cos(theta)
    Py = Oy + 4 * np.sin(theta)

    # Позиция точки на циклоиде
    x.append(Px - Ox)
    y.append(Py - Oy)

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 3*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y


def update(frame):
    xdata.append(2 * (frame - np.sin(frame)))
    ydata.append(2 * (1 - np.cos(frame)))
    anim_object.set_data(xdata, ydata)
    ball.set_data(circle_move(R=4, vx0 = 1.8, vy0=0.0001, time = frame))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='r', label ='triangle')
    anim_object, = plt.plot([], [], '-', lw=2)

    edge = 20
    plt.axis('equal')
    ax.set_xlim(0, edge)
    ax.set_ylim(-8, edge)

    ani = FuncAnimation(fig,
                    update,
                    frames=np.arange(0, 3*np.pi, 0.1),
                    interval=100
                    )

    
    ani.save('animation_11.gif')
# # Определение параметров циклоиды
# радиус = 1
# диаметр = 2 * радиус
# высота = 1

# # Создание массивов для хранения точек циклоиды
# x = []
# y = []

# # Шаг по времени
# dt = 0.01

# # Начальное положение точки на окружности
# theta = 0

# # Имитация движения точки и построение циклоиды
# while theta < 2*np.pi:
#     # Позиция центра окружности
#     Ox = диаметр * theta / (2*np.pi)
#     Oy = высота

#     # Позиция точки на окружности
#     Px = Ox + радиус * np.cos(theta)
#     Py = Oy + радиус * np.sin(theta)

#     # Позиция точки на циклоиде
#     x.append(Px - Ox)
#     y.append(Py - Oy)

#     # Обновление положения точки на окружности
#     theta += dt

# # Отрисовка циклоиды
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Циклоида')
# plt.show()
