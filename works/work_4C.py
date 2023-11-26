import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math

a = 2
b = 3

def x(t):
    return a * np.cos(t)


def y(t):
    return b * np.sin(t)


def dx_dt(t):
    return -a * np.sin(t)


def dy_dt(t):
    return b * np.cos(t)


def function(t):
    return np.sqrt(dx_dt(t)**2 + dy_dt(t)**2)


def ramun():
    return math.pi * (3*(a+b) - np.sqrt((3*a+b)*(a+3*b)))

length, _ = quad(function, 0, 2 * np.pi)

print(f"Длина эллипса с помощью дискретизации: {length:.6f}")

print(f"Длина эллипса по приближенной формуле Рамануджана: {ramun():.6f}")