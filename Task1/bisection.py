from Equation import Expression
import matplotlib.pyplot as plt
import numpy as np
import math
from unimodal_check import is_unimodal


def step_one(a, b):
    l = b-a
    x_1 = a + l/4.0
    x_2 = b - l/4.0
    x_0 = (a + b)/2.0
    return x_1, x_2, x_0

def bisec(fun,a,b,epsilon,it_limit):

    intervals = []
    x_0 = 0

    for k in range(it_limit):
       
        x_1,x_2,x_0 = step_one(a,b)
        intervals.append((a,b))
        
        vx_1 = fun(x_1)
        vx_0 = fun(x_0)
        vx_2 = fun(x_2)

        if abs(b - a) <= 2*epsilon:
            break

        elif vx_2 > vx_0 > vx_1:
            b = x_0
        elif vx_2 < vx_0 < vx_1:
            a = x_0
        else:
            a = x_1
            b = x_2
    return x_0,intervals

def mark_intervals(plot, interval,fun):
    for i,(start, end) in enumerate(interval):
        plot.scatter(start,fun(start), marker="|", linewidths=2, c='black')
        plot.scatter(end,fun(end), marker="|", linewidths=2, c='black')
        if i == len(interval)-1:
            break

    (start, end) = interval[-1]
    plot.scatter(start,fun(start), marker="|", linewidths=2, c='red')
    plot.scatter(end,fun(end), marker="|", linewidths=2, c='red')



def draw_bisection(fun, a, b, eps, it_limit):

    if is_unimodal(fun, a, b):
        x = np.linspace(a,b,200)
        y = fun(x)
        x_min, intervals = bisec(fun, a, b, eps, it_limit)
        y_min = fun(x_min)
        print('local:',x_min)
        print(intervals)

        # plotting the points
        # plt.plot(x_min,y_min,'ro')
        mark_intervals(plt, intervals, fun)
        plt.plot(x, y)

        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Minimum - Bisection')
        plt.figtext(0.5, 0.01, is_unimodal(fun,a,b), ha="center", fontsize=10, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
        plt.show()




draw_bisection(Expression("(1/2)*(4-2*x^2)*x^2",["x"]), -2, 2, 0.1, 40)
