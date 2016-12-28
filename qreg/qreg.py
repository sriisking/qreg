from scipy.optimize import minimize
import numpy as np

def minimizer_func(beta, fit_func, x_vals, q, observations):
    return q*np.sum(np.abs(np.where(observations>fit_func(beta, x_vals),observations - fit_func(beta, x_vals),0))) + \
           (1-q)*np.sum(np.abs(np.where(observations<fit_func(beta, x_vals),observations - fit_func(beta, x_vals),0)))

def quantile_regression(fit_func, x_vals, observations, beta_init, bounds=None, q_value = 0.5):
    res = minimize(minimizer_func, beta_init, args=(fit_func, x_vals, q_value, observations), bounds=bounds)
    return res

def func(beta, x):
    return beta[0]*np.power(x,2)

if __name__ == '__main__':
    x = np.array(range(5))
    y = 1.2*np.array(range(5))**2 + np.random.rand(5)
    print quantile_regression(func, x, y, [1], q_value=.5)

#API -
#R1 score
#Other diagnostic
#Multi parameter analysis