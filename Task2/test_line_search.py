import numpy as np
import numdifftools as nd
from scipy.optimize import line_search

def fun(x): 
    return x[0]**2 + 4*x[1]**2

def get_alpha(fun,current_point):
  
    def grad(x):
        return  nd.Gradient(fun)([x[0],x[1]])
    x = np.ravel(current_point)
    p = -grad(x) #current search direc
    a = line_search(fun, grad, x, p)[0]

    print(a)

get_alpha(fun,np.array([[1.],[3.]]))