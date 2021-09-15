import numpy as np
import matplotlib.pyplot as plt

a = np.array([2, 3])

A = np.array([[2, -1],
              [2, -2]])

b = np.dot(A, a)

def arrow(start, vector, color):
    plt.quiver(start[0], start[1], vector[0], vector[1], color=color,
               angles='xy', scale_units='xy', scale=1)

s = np.array([0, 0])

arrow(s, a, color='black')
arrow(s, a, color='blue')

plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.xlabel('x', size=15)
plt.ylabel('y', size=15)
plt.grid()
plt.gca().set_aspect('equal') # 가로세로비를 같게 (gca: get current axes)
plt.show()
