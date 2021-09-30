import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi / 2, np.pi / 2) # -pi/2 ~ pi/2
T = (np.sin(X) + 1) / 2 # 0 ~ 1
n_data = len(X)

def forward(x, w, b):
    u = w*x + b
    y = 1/(1+np.exp(-u))
    return y

def backward(x, y, t):
    delta = (y - t) * (1 - y) * Y
    grad_w = x * delta
    grad_b = delta
    return (grad_w, grad_b)

def show_output(X, Y, T, epoch):
    plt.plot(X, T, linestyle='dashed')
    plt.scatter(X, Y, marker='+')
    
    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    plt.grid()
    plt.show()

    print('Epoch:', epoch)
    print('Error:', 1/2 * np.sum((Y-T)**2))

eta = 0.1
epoch = 100

w = 0.2
b = -0.2

for i in range(epoch):
    if i < 10:
        Y = forward(X, w, b)
        show_output(X, Y, T, i)

    idx_rand = np.arange(n_data)
    np.random.shuffle(idx_rand)

    for j in idx_rand:
        x = X[j]
        t = T[j]

        y = forward(x, w, b)
        grad_w, grad_b = backward(x, y, t)
        w -= eta * grad_w
        b -= eta * grad_b

Y = forward(X, w, b)
show_output(X, Y, T, epoch)