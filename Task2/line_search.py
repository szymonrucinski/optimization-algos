from scipy.optimize import minpack2
import numpy as np
from numpy.compat import asbytes
import numdifftools as nd
import numpy as np
from scipy.optimize import line_search

def get_alpha(fun, current_point, direction):

    alpha_gradient = lambda point : nd.Gradient(fun)([point[0],point[1]])
    x = current_point.flatten()
    direction = alpha_gradient(current_point)

    # print(x)
    # print(alpha_gradient)
    # print(direction)

    a = line_search(fun, alpha_gradient, x, direction)[0]
    return a
