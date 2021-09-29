import numpy as np
import matplotlib.pyplot as plt

def pdf(x, mu, sigma):
    return 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))

x = np.linspace(-5, 5)
y_1 = pdf(x, 0.0, 0.5)
y_2 = pdf(x, 0.0, 1.0)
y_3 = pdf(x, 0.0, 2.0)

plt.plot(x, y_1, label='sigma: 0.5', linestyle='dashed')
plt.plot(x, y_2, label='sigma: 1.0', linestyle='solid')
plt.plot(x, y_3, label='sigma: 2.0', linestyle='dashdot')
plt.legend()

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()