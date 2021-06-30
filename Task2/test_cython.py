import cython

from cython_gsl import *

from libc.math import pow

cdef double min_f(double x, void * params) nogil:
    # Extract params
    cdef double * ps = <double *> params
    # Compute penalty
    cdef double penalty = pow(ps[0], ps[1])

    cdef double f = pow(x, 2)

    # If outside feasible region, add the penalty
    if 0 > (x - 1):
        f = f + 1 / penalty * pow(x - 1, 2)

    return f