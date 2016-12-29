from scipy.optimize import minimize
import numpy as np

def minimizer_func(beta, fit_func, x_vals, q, observations):
    return q*np.sum(np.abs(np.where(observations>fit_func(beta, x_vals),observations - fit_func(beta, x_vals),0))) + \
           (1-q)*np.sum(np.abs(np.where(observations<fit_func(beta, x_vals),observations - fit_func(beta, x_vals),0)))

def quantile_regression(fit_func, x_vals, observations, beta_init, bounds=None, q_value = 0.5):
    return minimize(minimizer_func, beta_init, args=(fit_func, x_vals, q_value, observations), bounds=bounds)

#API -
#Object oriented design
#R1 score
#Other diagnostic
#Multi parameter analysis
#Add fit predict