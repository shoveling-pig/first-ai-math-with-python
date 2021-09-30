import numpy as np
import matplotlib.pyplot as plt

def power_func(x, c, k):
    return c*x**(-k)

x = np.linspace(1, 5)
y_1 = power_func(x, c=1.0, k=1.0)
y_2 = power_func(x, c=1.0, k=2.0)
y_3 = power_func(x, c=1.0, k=4.0)

plt.plot(x, y_1, label='k=1.0', linestyle='dashed')
plt.plot(x, y_2, label='k=2.0', linestyle='solid')
plt.plot(x, y_3, label='k=4.0', linestyle='dashdot')
plt.legend()

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()