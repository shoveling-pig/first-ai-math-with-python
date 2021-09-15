import numpy as np

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

a = np.array([1, 1, 1, 1])

b = np.array([2, 2, 2, 2])

c = np.array([-1, -1, -1, -1])

print(cos_sim(a, b))

print(cos_sim(a, c))
