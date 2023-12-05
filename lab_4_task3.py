g = 10

def energy_func(m, h, v):
     E = m * g * h + m * v**2 / 2
     return E


print(energy_func(1, 8, 9))


