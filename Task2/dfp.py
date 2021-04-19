import numpy as np
import copy
import math
import numdifftools as nd
from line_search import get_alpha
#http://sms.am.put.poznan.pl/wp-content/uploads/2019/12/POPK_03.pdf
#https://slideplayer.com/slide/4260069/


def fun(xy): 
    return 100*(xy[1]**2 - xy[0]**2)+(1-xy[0]**2)

def gradient(point):
    result = nd.Gradient(fun)([point[0],point[1]])
    return result.reshape(-1,1)

def M(current_hessian_approx,q):
    numerator = np.linalg.multi_dot([current_hessian_approx,q,q.transpose(),current_hessian_approx])
    denominator = np.linalg.multi_dot([q.transpose(),current_hessian_approx,q])
    return np.divide(numerator,denominator)

def N(p,q):
    numerator = p.dot(p.transpose())
    denominator = np.dot(p.transpose(),q)
    N = np.divide(numerator, denominator)
    return N

#Gradient approximation
def update_hessian_approx(current_hessian_approx,delta_gradient, delta_x):
    p = delta_x
    q = delta_gradient
    # return current_hessian_approx + N(p,q) - M(current_hessian_approx,q)
    return current_hessian_approx + N(p,q) -  M(current_hessian_approx,q)

def stop_fpd(current_gradient,eps):
    vector = current_gradient.flatten()
    return math.sqrt(vector[0]**2 + vector[1]**2)< eps

def fpd(x,y,it_num, eps):
    #Dokładność
    #Macierz 2x2 o dodatnim wyznaczniku lub jednostkowa
    hessian_approx = np.identity(2)
    point = np.array([[x,y]],np.float64).transpose()
 
    for i in range(0,it_num):
        current_gradient = gradient(point)
        #1) Compute approx. Newton , update direction
        direction = -1 * np.dot(hessian_approx, current_gradient)
        #2) Line search (inexact)
        points = []
        points.append(point)
        alpha = get_alpha(fun, point, direction)
        ###(function)
        point = point - np.dot(alpha,direction)
        points.append(point)
        delta_x = points[0] - points[1]
        #3) Computer gradient for point x_(i+1)
        next_gradient = gradient(point)
        delta_gradient = current_gradient - next_gradient 
        #4) Update Hessian
        hessian_approx = update_hessian_approx(hessian_approx, delta_gradient, delta_x)
        print(hessian_approx)

        if stop_fpd(current_gradient, eps):
            break

fpd(x = -1, y = -1 ,it_num = 35, eps = 0.01)
