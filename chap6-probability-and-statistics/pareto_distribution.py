# Reference
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.pareto.html

import numpy as np
import matplotlib.pyplot as plt

s = np.random.pareto(4, 1000)

plt.hist(s, bins=25)
plt.xlabel('x', size=14)
plt.grid()

plt.show()