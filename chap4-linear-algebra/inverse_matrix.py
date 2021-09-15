import numpy as np

a = np.array([[1, 1],
              [1, 2]])

determinant = np.linalg.det(a)

if determinant:
    inv_matrix = np.linalg.inv(a)
    print(inv_matrix)
