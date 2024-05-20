import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('H.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

t0 = np.linspace(np.pi-np.pi/8, np.pi/1.8, 100)
x0 = 400 + 240 * np.cos(t0)
y0 = 800 - 240 * np.sin(t0)
ax.plot(x0, y0, '-', lw=2, color = 'k')


t1 =  np.linspace(3 * np.pi/2, 2 * np.pi, 200)
x1 = 360 + 115 * np.cos(t1)
y1 = 348 - 215 * np.sin(t1)
ax.plot(x1, y1, '-', lw=2, color = 'k')

x = np.append(x0, x1)
y = np.append(y0, y1)


x2 = [475, 385]
y2 = [350, 370]
ax.plot(x2, y2, '-', lw=2, color = 'k')

x = np.append(x, x2)
y = np.append(y, y2)

t3 =  np.linspace(3 * np.pi/2, np.pi/2, 200)
x3 = 380 + 60 * np.cos(t3)
y3 = 320 - 50 * np.sin(t3)
ax.plot(x3, y3, '-', lw=2, color = 'k')

x = np.append(x, x3)
y = np.append(y, y3)

t4 =  np.linspace (3 * np.pi/2, 2 * np.pi,200)
x4 = 380 + 100 * np.cos(t4)
y4 = 160 - 109.9 * np.sin(t4)
ax.plot(x4, y4, '-', lw=2, color = 'k')

x = np.append(x, x4)
y = np.append(y, y4)

t5 =  np.linspace( np.pi,  3 * np.pi/2,200)
x5 = 610 + 130 * np.cos(t5)
y5= 155 - 45 * np.sin(t5)
ax.plot(x5, y5, '-', lw=2, color = 'k')

x = np.append(x, x5)
y = np.append(y, y5)

t6 =  np.linspace( 5 * np.pi/2, 2 * np.pi,200)
x6 = 610.05 + 105 * np.cos(t6)
y6 = 300 - 100 * np.sin(t6)
ax.plot(x6, y6, '-', lw=2, color = 'k')

x = np.append(x, x6)
y = np.append(y, y6)

x7 = [715, 690]
y7 = [300, 580]
ax.plot(x7, y7, '-', lw=2, color = 'k')

x = np.append(x, x7)
y = np.append(y, y7)


t8 =  np.linspace(np.pi/2, np.pi,  200)
x8 = 690.05 + 60 * np.cos(t8)
y8 = 705 - 125 * np.sin(t8)
ax.plot(x8, y8, '-', lw=2, color = 'k')

x = np.append(x, x8)
y = np.append(y, y8)

# x9 = [620, 180]
# y9 = [718, 718]

# x = np.append(x, x9)
# y = np.append(y, y9)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
# figure_spline_part_manual = np.arange(0, 0.5, 0.01)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])


polygon = geom.Polygon(curve_coords)
points_number_per_side = 400
x_pictures_limits = [0, 1010]
y_pictures_limits = [720, 0]

points_coords = []
for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_func = intensity * np.exp(- dec_rate[0]*x**2 - dec_rate[1]*y**2) 
    return scalar_func

intensity_centerums_x = [250, 320, 400, 450, 500, 560, 500, 490, 500, 490, 490, 490, 520, 550, 600, 650, 700, 650, 600]
intensity_centerums_y = [650, 600, 580, 600, 560, 530, 450, 400, 340, 320, 280, 470, 290, 295, 290, 290, 290, 300, 300]
intensity_values =      [0.7, 0.9, 0.5, 0.7, 0.5, 0.5, 0.5, 0.2, 0.5, 0.5, 0.5, 0.5, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.5]
def scalar_function(x, y, int_cen_x, int_cen_y, int_vel):
    scalar_field = 0.0
    for i in range(0, len(int_cen_x)):
        scalar_field += int_vel[i] * bell_function(x-int_cen_x[i], y-int_cen_y[i], 30, [0.000109, 0.000109])
    return scalar_field

scalar_fields = []
for i in range(0, len(x_p)):
    calculate = scalar_function(x_p[i], y_p[i], intensity_centerums_x, 
                                intensity_centerums_y, intensity_values)
    scalar_fields.append(calculate)
   
fig, ax = plt.subplots()
sc_plot = ax.scatter(x_p, y_p, c=scalar_fields)
plt.plot(spline_curve[0], spline_curve[1], 'm', lw=4)
plt.axis('equal')
plt.ylim(700, 0)
cbar = fig.colorbar(sc_plot)
plt.savefig('horse1.png')
