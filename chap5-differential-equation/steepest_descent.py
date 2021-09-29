import numpy as np
import matplotlib.pyplot as plt

def my_func(x):
    return x**4 - 2*x**3 - 3*x**2 + 2*x

def grad_func(x):
    return 4*x**3 - 6*x**2 - 6*x + 2

eta = 0.01
x = 1.0
record_x = []
record_y = []

for i in range(20):
    y = my_func(x)
    record_x.append(x)
    record_y.append(y)
    x -= eta * grad_func(x)

x_f = np.linspace(-1.6, 2.8)
y_f = my_func(x_f)

plt.plot(x_f, y_f, linestyle='dashed')
plt.scatter(record_x, record_y)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.show()