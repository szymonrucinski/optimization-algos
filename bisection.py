from Equation import Expression
import matplotlib.pyplot as plt
import numpy as np


def step_one(a, b):
    l = a - b
    x_1 = (a + l)/4.0
    x_2 = (b - l)/4.0
    x_0 = (a + b)/2.0
    return x_1, x_2, x_0

def bisec(fun,a,b,epsilon,it_limit):

    x_0 = 0
    for k in range(it_limit):
       
        x_1,x_2,x_0 = step_one(a,b)

        if abs(b - a) <= 2*epsilon:
            break

        elif fun(x_1) < fun(x_2):
            b = x_0
        elif fun(x_2) < fun(x_0):
            a = x_0
        else:
            a = x_1
            b = x_2
    return x_0


def draw_bisection(fun, a, b, eps, it_limit):

    x = np.linspace(a,b,200)
    y = fun(x)
    print(fun(x), print(y))

    x_min = bisec(fun, a, b, eps, it_limit)
    print(type(x_min))
    y_min = fun(x_min)

    # plotting the points
    plt.plot(x_min,y_min,'ro')  
    plt.plot(x, y)
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Minimum')
    
    plt.show()



# draw_bisection(Expression("x^2 +2",["x"]), -6, 10, 0.1, 20)
