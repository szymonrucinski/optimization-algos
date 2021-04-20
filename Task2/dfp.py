import numpy as np
import copy
import math
import numdifftools as nd
from line_search import get_alpha
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
#http://sms.am.put.poznan.pl/wp-content/uploads/2019/12/POPK_03.pdf
#https://slideplayer.com/slide/4260069/


def fun(x): 
    return 4*x[0]**2 + x[1]**2 - 2*x[0]*x[1]

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
    return current_hessian_approx + N(p,q) - M(current_hessian_approx,q)

def stop(current_gradient,eps):
    vector = current_gradient.flatten()
    return math.sqrt(vector[0]**2 + vector[1]**2) < eps


def print_in_console(point, gradient,hessian):
    print(f'POINTS: {point.flatten()}\n')
    print(f'GRADIENT: {gradient.flatten()}\n')
    print("HESSIAN:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in hessian]))
    print("=============================================")

def plot_graph(progress_x, progress_y):
    fig = plt.figure()
    f = lambda x,y: 4 * np.power(x,2) + np.power(y,2) - 2 * x * y
    ax = plt.axes(projection="3d")
    points = np.linspace(-5,5,20)
    X,Y = np.meshgrid(points, points)
    Z = f(X,Y)

    P_X, P_Y = np.meshgrid(progress_x,progress_y)
    P_Z = f(P_X,P_Y)
    # reversed colorbar because of the bug present in matplotlib indexing.
    p = ax.scatter(P_X,P_Y,P_Z,c=P_Z,cmap='viridis_r',s=20)
    fig.colorbar(p, ax=ax)
  
    ax.plot_wireframe(X,Y,Z)
    plt.show()


def dfp(x,y,it_num, eps):
    #Dokładność
    #Macierz 2x2 o dodatnim wyznaczniku lub jednostkowa
    hessian_approx = np.identity(2)
    point = np.array([[x,y]],np.float64).transpose()
    #store points
    progress_x = []
    progress_y = []

    for i in range(0,it_num):
        current_gradient = gradient(point)
        #1) Compute approx. Newton , update direction
        direction = -1 * np.dot(hessian_approx, current_gradient)
        points = []
        points.append(point)
        #2) Line search to get alpha ~ most optimal "step lenght"
        alpha = get_alpha(fun, point)
        #3) approximate new point
        point = point + np.dot(alpha,direction)
        points.append(point)
        delta_x = points[1] - points[0]
        #4) Compute gradient for new point
        next_gradient = gradient(point)
        delta_gradient = next_gradient - current_gradient 
        #5) Update inverse Hessian
        hessian_approx = update_hessian_approx(hessian_approx, delta_gradient, delta_x)
        
        #store points  coordinates as the evaluation progresses used to plot progress
        progress_x.extend((points[0][0], points[1][0]))
        progress_y.extend((points[0][1], points[1][1]))

        print_in_console(points[0], current_gradient, hessian_approx)
        if stop(current_gradient, eps):
            break
    plot_graph(np.asarray(progress_x), np.asarray(progress_y))


# dfp(x = -5., y = -5 ,it_num = 45, eps = 0.5)

