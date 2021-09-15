import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([3, 2, 1])

result1 = np.dot(v1, v2)
result2 = np.sum(v1 * v2)

print(result1 == result2)

m1 = np.array([[0, 1, 2],
              [1, 2, 3]])

m2 = np.array([[2, 1],
              [2, 1],
              [2, 1]])

result = np.dot(m1, m2)

print(result)
