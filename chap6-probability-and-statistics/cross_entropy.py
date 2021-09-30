import numpy as np

delta = 1e-7

def cross_entropy(p, t):
    return -np.sum(t*np.log(p+delta) + (1-t)*np.log(1-p+delta))

p_1 = np.array([0.2, 0.8, 0.1, 0.3, 0.9, 0.7])
p_2 = np.array([0.7, 0.3, 0.9, 0.8, 0.1, 0.2])
t = np.array([1, 0, 1, 1, 0, 0])

print('p_1:', cross_entropy(p_1, t))
print('p_2:', cross_entropy(p_2, t))