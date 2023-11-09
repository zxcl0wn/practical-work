from math import *
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 8*x + 1 - 5*sin(x)

start = -5
end = 5

step = 0.0001
zxc = set()
x = start

x_values = []
f_values = []

while x <= end:
    result = f(x)
    x_values.append(x)
    f_values.append(result)
    if abs(result) <= 0.001:
        number = f'{x:.3f}'
        zxc.add(float(number))
    x += step

for i in zxc:
    print("Интервал [-5; 5]")
    print(f"Решение: {i}\n")

# Построение графика
plt.figure()
plt.plot(x_values, f_values, label='f(x)')
plt.axhline(0, color='r', linestyle='--', label='y=0')


for i in zxc:
    plt.scatter(i, f(i), color='g', label='Решение', marker='o')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График уравнения')
plt.grid()
plt.legend()

plt.show()