from Equation import Expression
import matplotlib.pyplot as plt

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



def bisection_test(fun, a, b, eps, it_limit):
        # x axis values
    x = [1,2,3]
    # corresponding y axis values
    y = [2,4,1]
    
    # plotting the points 
    plt.plot(x, y)
    
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
    # giving a title to my graph
    plt.title('My first graph!')
    
    # function to show the plot
    plt.show()

# fun = Expression("(x-3)^2", ["x"])
# print(fun)
# a = bisec(fun, 0, 150, 0.02, 10)
# print(a)
