import numpy as np
import matplotlib.pyplot as plt

def approach_napier(n):
    return (1 + 1/n)**n

n_list = [2, 4, 10]
for n in n_list:
    print('a_' + str(n) + ' =', approach_napier(n))

x = np.linspace(-2, 2)
y = np.exp(x)

plt.plot(x, y)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.show()
