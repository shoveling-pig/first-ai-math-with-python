import numpy as np
import matplotlib.pylab as plt

def sigmoid_function(x):
    return 1/(1 + np.exp(-x))

def grad_sigmoid(x):
    y = sigmoid_function(x)
    return (1-y)*y

x = np.linspace(-5, 5)
y = sigmoid_function(x)
y_grad = grad_sigmoid(x)

plt.plot(x, y, label='y')
plt.plot(x, y_grad, label='y_grad')
plt.legend()
plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.show()