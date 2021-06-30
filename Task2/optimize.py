import scipy.optimize

banana = lambda x: 4*x[0]**2 + x[1]**2 - 2*x[0]*x[1]
xopt = scipy.optimize.fmin(func=banana, x0=[10,10])
print(xopt)