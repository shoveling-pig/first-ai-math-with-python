import numpy as np
import matplotlib.pyplot as plt

def show_cov(cov):
    print('--- Covariance:', cov, ' ---')
    
    average = np.array([0, 0])
    cov_matrix = np.array([[1, cov],
                          [cov, 1]])
    
    data = np.random.multivariate_normal(average, cov_matrix, 3000)
    x = data[:, 0]
    y = data[:, 1]

    plt.scatter(x, y, marker='x', s=20)
    
    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    plt.grid()

    plt.show()

show_cov(0.6)
show_cov(0.0)
show_cov(-0.6)