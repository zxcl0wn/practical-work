import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve


def f1(x):
    return x ** 3 - 8 * x + 1


def f2(x):
    return 5 * np.sin(x)


initial_guesses = [-5, 0, 5]

roots_real = fsolve(lambda x: f1(x) - f2(x), initial_guesses)
x_values = np.linspace(-5, 5, 100)
y_values1 = [f1(x) for x in x_values]
y_values2 = [f2(x) for x in x_values]

plt.plot(x_values, y_values1, label='$x^3 - 8x + 1$')
plt.plot(x_values, y_values2, label='$5*sin(x)$')

plt.scatter(roots_real, [f2(root) for root in roots_real], color='blue', label='Roots')

x_fill = np.linspace(roots_real[0], roots_real[2], 100)
plt.fill_between(x_fill, f1(x_fill), f2(x_fill), color='green', alpha=0.3, label='Shaded area')


plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функций')
plt.show()

area1 = abs(np.trapz(f1(x_fill), x=x_fill))
area2 = abs(np.trapz(f2(x_fill), x=x_fill))
print(f"Площадь 1 способом: {(area1+area2):4f}")

area1, _ = quad(lambda x: f1(x), min(roots_real), max(roots_real))
area2, _ = quad(lambda x: f2(x), min(roots_real), max(roots_real))
print(f"Площадь 2 способом: {(abs(area1) + abs(area2)):4f}")