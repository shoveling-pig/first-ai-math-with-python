import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 2)
y = np.log(x)

plt.plot(x, y)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()