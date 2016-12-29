from qreg import qreg
import numpy as np

def func(beta, x):
    return beta[0]*np.power(x,2)

if __name__ == '__main__':
    x = np.array(range(5))
    y = 1.2*np.array(range(5))**2 + np.random.rand(5)
    print qreg.quantile_regression(func, x, y, [1], q_value=.5)