import numpy as np
import matplotlib.pyplot as plt

x = np.array([50, 70, 40, 60, 80])
y = np.array([60, 80, 50, 50, 70])
z = np.array([60, 40, 60, 40, 30])

cov_xy = np.average( (x - np.average(x)) * (y - np.average(y)) )
print('cov_xy', cov_xy)

cov_xz = np.average( (x - np.average(x)) * (z - np.average(z)) )
print('cov_xz', cov_xz)

plt.scatter(x, y, marker='o', label='xy', s=50)
plt.scatter(x, z, marker='x', label='xz', s=50)
plt.legend()

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()