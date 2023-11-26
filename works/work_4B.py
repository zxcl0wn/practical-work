import math

v = float(input('Введите скорость полета шарика: '))
t = float(input('Введите время полета шарика: '))

g1 = 35.5
g2 = 65.8

s1 = t * v * math.cos(math.radians(g1))
s2 = t * v * math.cos(math.radians(g2))

print(f"s1 = {s1:.3f} м")
print(f"s2 = {s2:.3f} м")