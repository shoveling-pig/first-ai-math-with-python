import numpy as np

a = np.array([-2, -1, 1, 2])

print(np.linalg.norm(a)) # default norm is L2 
print(np.linalg.norm(a, 1))
