from Equation import Expression
import matplotlib.pyplot as plt
import numpy as np


def step_one(a, b):
    x_0 = (a + b) / 2
    x_1 = (a + x_0) / 2
    x_2 = (b + x_0) / 2
    L = b - a
    return x_1, x_0, x_2


def bisec(fun, a, b, eps, it_limit):
    # |----|----|----|----|
    # A   x_1   x_0  x_2  B

    a = a
    b = b
    x_1, x_0, x_2 = step_one(a, b)
    iterations_made = 0

    while abs(b - a) >= 2 * eps:
        if iterations_made == it_limit:
            break
        else:
            iterations_made = iterations_made + 1
        print("calculation for", a, b)
        # Jezeli spelniony jest ten warunek odrzuc przedial (x_0,b)
        if fun(x_2) > fun(x_0) > fun(x_1):
            b = x_0
            x_1, x_0, x_2 = step_one(a, b)
            continue

        # Jezeli spelniony jest ten warunek odrzuc przedial (a,x_0)
        elif fun(x_2) < fun(x_0) < fun(x_1):
            a = x_0
            x_1, x_0, x_2 = step_one(a, b)
            continue

        elif fun(x_1) > fun(x_0) and fun(x_2) > fun(x_1):
            a = x_1
            b = x_2
            x_1, x_0, x_2 = step_one(a, b)
            continue
        else:
            break

    return x_0



def draw_bisection(fun, a, b, eps, it_limit):

    x = np.linspace(a,b,200)
    y = fun(x)

    x_min = bisec(fun,a,b,eps,it_limit)
    y_min = fun(x_min)

    # plotting the points
    plt.plot(x_min,y_min,'ro')  
    plt.plot(x, y)
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Minimum')
    
    plt.show()
