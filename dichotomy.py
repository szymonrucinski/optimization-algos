from Equation import Expression
import matplotlib.pyplot as plt
import numpy as np


def step_fun(a, b, delta):
    x0 = (a + b) / 2
    x1 = x0 - (delta / 2)
    x2 = x0 + (delta / 2)
    return x0, x1, x2


def dicho(fun, a, b, delta, it_limit):
    # |------|---|---|------|
    # A    x0-d  x0 x0+d    B

    x0, x1, x2 = step_fun(a, b, delta)
    iterations = 0

    while abs((a + b) / 2) > delta and iterations <= it_limit:
        iterations = iterations + 1

        if fun(x1) < fun(x2):
            b = x0
            x0, x1, x2 = step_fun(a, b, delta)
            continue

        elif fun(x1) >= fun(x2):
            a = x0
            x0, x1, x2 = step_fun(a, b, delta)
            continue

        else:
            break
    print(x0)
    return x0


def draw_dichotomy(fun, a, b, delta, it_limit):
    x = np.linspace(a, b, 200)
    y = fun(x)

    x_min = dicho(fun, a, b, delta, it_limit)
    y_min = fun(x_min)

    print("Local Minimum of the function in interval", a, ",", b, " is a point: (", x_min, ", ", y_min, ").")

    # plotting the points
    plt.plot(x_min, y_min, 'ro')
    plt.plot(x, y)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Minimum')

    plt.show()

