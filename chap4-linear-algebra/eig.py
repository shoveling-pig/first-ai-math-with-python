import numpy as np

a = np.array([[3, 1],
              [2, 4]])

eig = np.linalg.eig(a)

# 고유값 리스트
eigen_values = eig[0]
print(eigen_values)

# 고유벡터 리스트
eigen_vectors = eig[1]
print(eigen_vectors)
