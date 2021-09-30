import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([2.4, 1.2, 3.5, 2.1, 4.7])

mu = np.average(x_data)
sigma = np.std(x_data)\

def pdf(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))

def log_likelihood(pdf):
    return np.sum(np.log(pdf))

x_sigma = np.linspace(0.5, 8)
y_loglike = [log_likelihood(pdf(x_data, mu, s)) for s in x_sigma]

plt.plot(x_sigma, np.array(y_loglike))
plt.plot([sigma, sigma], [min(y_loglike), max(y_loglike)], linestyle='dashed')

plt.xlabel('x_sigma', size=14)
plt.ylabel('y_loglike', size=14)
plt.grid()

plt.show()
