import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def f(x):
    return x**2

def df(x):
    return 2*x

def function(x):
    return np.sqrt(1 + (df(x))**2)

a, b = 0, 10

length, _ = quad(function, a, b)

print(f"Длина кривой: {length:.4f}")

x_values = np.linspace(a, b, 100)
y_values = f(x_values)

plt.plot(x_values, y_values, label='$y = x^2$')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()




