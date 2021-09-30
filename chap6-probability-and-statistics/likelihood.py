import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([2.4, 1.2, 3.5, 2.1, 4.7])
y_data = np.zeros(5)

mu = np.average(x_data)
sigma = np.std(x_data)

def pdf(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))

x_pdf = np.linspace(-3, 7)
y_pdf = pdf(x_pdf, mu, sigma)

plt.scatter(x_data, y_data)
plt.plot(x_pdf, y_pdf)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()

print('\n--- Likelihood ---')
print(np.prod(pdf(x_data, mu, sigma)))

print('\n--- Log Likelihood ---')
print(np.sum(np.log(pdf(x_data, mu, sigma))))
