from scipy.optimize import minpack2
import numpy as np
from numpy.compat import asbytes
import numdifftools as nd
import numpy as np
from scipy.optimize import line_search

def get_alpha(fun,current_point):
  
    def grad(x):
        return  nd.Gradient(fun)([x[0],x[1]])
    x = np.ravel(current_point)
    p = -grad(x) #current search direc
    a = line_search(fun, grad, x, p)[0]
    return a

# line_search(fun,np.array([1.],[3.]),)