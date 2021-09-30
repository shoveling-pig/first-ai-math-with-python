import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi)
T = np.sin(X)

# Add gaussian noise
T += 0.4 * np.random.randn(len(X))

# Resize X
X /= np.pi

eta = 0.01

def polynomial(x, params):
    return sum([params[i]*x**i for i in range(len(params))])

def grad_params(X, T, params):
    grad_ps = np.zeros(len(params))
    for i in range(len(params)):
        for j in range(len(X)):
            grad_ps[i] += ( polynomial(X[j], params) - T[j] ) * X[j] ** i
    return grad_ps

def fit(X, T, degree, epoch):
    params = np.random.randn(degree + 1)
    for i in range(len(params)):
        params[i] *= 2**i

    for i in range(epoch):
        params -= eta * grad_params(X, T, params)
    
    return params

degrees = [1, 3, 6]
for degree in degrees:
    print('--- ' + str(degree) + ' ---')
    params = fit(X, T, degree, 1000)
    Y = polynomial(X, params)
    plt.scatter(X, T)
    plt.plot(X, Y, linestyle='dashed')
    plt.show()
