# Reference
# https://en.wikipedia.org/wiki/Pearson_correlation_coefficient


import numpy as np
import matplotlib.pyplot as plt

x = np.array([30, 70, 40, 60, 90])
y = np.array([20, 60, 50, 40, 80])

print('--- 공분산과 표준편차를 사용하여 구한 상관계수 ---')
cov_xy = np.average( (x - np.average(x)) * (y - np.average(y)) )
print(cov_xy / (np.std(x) * np.std(y)))
print()

print('--- np.corrcoef() 함수를 사용하여 구한 상관계수 ---')
print(np.corrcoef(x, y))

plt.scatter(x, y)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()
