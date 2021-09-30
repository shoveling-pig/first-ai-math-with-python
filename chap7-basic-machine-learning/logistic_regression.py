import numpy as np
import matplotlib.pyplot as plt

n_data = 500
X = np.zeros((n_data, 2))
T = np.zeros((n_data))

for i in range(n_data):
    x_rand = np.random.rand()
    y_rand = np.random.rand()
    X[i, 0] = x_rand
    X[i, 1] = y_rand
    
    if x_rand > y_rand + 0.2 * np.random.randn():
        T[i] = 1

eta = 0.01

def classify(x, a_params, b_param):
    u = np.dot(x, a_params) + b_param
    return 1 / (1 + np.exp(-u))

def cross_entropy(Y, T):
    delta = 1e-7
    return -np.sum(T * np.log(Y+delta) + (1-T) * np.log(1-Y+delta))

def grad_a_params(X, T, a_params, b_param):
    grad_a = np.zeros(len(a_params))
    for i in range(len(a_params)):
        for j in range(len(X)):
            grad_a[i] += ( classify(X[j], a_params, b_param) - T[j] ) * X[j, i]
    return grad_a

def grad_b_params(X, T, a_params, b_param):
    grad_b = 0
    for i in range(len(X)):
        grad_b += ( classify(X[i], a_params, b_param) - T[i] )
    return grad_b

error_x = []
error_y = []

def fit(X, T, dim, epoch):
    a_params = np.random.randn(dim)
    b_param = np.random.randn()

    for i in range(epoch):
        grad_a = grad_a_params(X, T, a_params, b_param)
        grad_b = grad_b_params(X, T, a_params, b_param)
        a_params -= eta * grad_a
        b_param -= eta * grad_b

        Y = classify(X, a_params, b_param)
        error_x.append(i)
        error_y.append(cross_entropy(Y, T))
    
    return (a_params, b_param)

a_params, b_param = fit(X, T, 2, 200)
Y = classify(X, a_params, b_param)

result_x = []
result_y = []
result_z = []

for i in range(len(Y)):
    result_x.append(X[i, 0])
    result_y.append(X[i, 1])
    result_z.append(Y[i])

print('--- Probability Distribution ---')
plt.scatter(result_x, result_y, c=result_z)
plt.colorbar()
plt.show()

print('--- trend of error ---')
plt.plot(error_x, error_y)
plt.xlabel('Epoch', size=14)
plt.ylabel('Cross Entropy', size=14)
plt.show()
