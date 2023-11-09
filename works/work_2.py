import math
import matplotlib.pyplot as plt
import numpy as np

def find_root_using_bisection(f, start, end, eps):
    delta = 2 * eps
    step = 0
    while end - start > delta:
        step += 1
        c = (start + end) / 2
        if f(start) * f(c) <= 0:
            end = c
        else:
            start = c
    mid = (start + end) / 2
    return mid, step

def f(x):
    return x**3 - 8*x + 1 - 5*math.sin(x)

start = -5
end = 5
zxc = set()

eps = 0.0001

x_values = np.linspace(start, end, 1000)
f_values = [f(x) for x in x_values]

plt.figure()
plt.plot(x_values, f_values, label='f(x)')
plt.axhline(0, color='r', linestyle='--', label='y=0')

x = start

while x < end:
    if f(x) * f(x + 1) <= 0.001:
        mid, step = find_root_using_bisection(f, x, x + 1, eps)
        plt.scatter(mid, 0, color='g', label='Решение', marker='o')
        print(f"Интервал [{x:.3f}; {x + 1:.3f}]")
        print(f"Решение: {mid:.3f}")
        print(f"Число шагов: {step}\n")
    x += 1

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График уравнения')
plt.grid()
plt.legend()

plt.show()