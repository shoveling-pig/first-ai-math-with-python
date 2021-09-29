import numpy as np
import matplotlib.pyplot as plt

def my_func(x):
    return -2*x**2 + x + 3

def my_func_diff(x):
    return -4*x + 1

x = np.linspace(-3, 3)
y = my_func(x)

a = 1
y_t = my_func_diff(a)*x + my_func(a) - my_func_diff(a)*a

plt.plot(x, y, label='y')
plt.plot(x, y_t, label='y_t')

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.legend()
plt.show()