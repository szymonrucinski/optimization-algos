from Equation import Expression
import matplotlib.pyplot as plt
import numpy as np

from unimodal_check import is_unimodal

def step_fun(a, b, delta):
    x0 = (a + b) / 2
    x1 = x0 - (delta / 2)
    x2 = x0 + (delta / 2)
    return x0, x1, x2


def dicho(fun, a, b, delta, it_limit):
    # |------|---|---|------|
    # A    x0-d  x0 x0+d    B

    interval_list = []
    x0, x1, x2 = step_fun(a, b, delta)
    iterations = 1
    interval_list.append(a)
    interval_list.append(b)

    while abs((a - b) / 2) > delta and iterations < it_limit:
        iterations = iterations + 1

        if fun(x1) < fun(x2):
            b = x0
            x0, x1, x2 = step_fun(a, b, delta)

        elif fun(x1) >= fun(x2):
            a = x0
            x0, x1, x2 = step_fun(a, b, delta)

        else:
            break
        interval_list.append(a)
        interval_list.append(b)
    print(x0)
    return x0, interval_list


def draw_dichotomy(fun, a, b, delta, it_limit):

    if is_unimodal(fun, a, b):
        x = np.linspace(a, b, 200)
        y = fun(x)

        x_min, interval_list = dicho(fun, a, b, delta, it_limit)
        y_min1 = fun(x_min-delta)
        y_min2 = fun(x_min+delta)

        print(f"Local Minimum of the function in interval ({a}, {b}) is in an interval between points:"
              f" ( {x_min}, {y_min1} ), and ({x_min}, {y_min2}).")

        # plotting the points

        plt.plot(x, y)
        i = 0
        while i < len(interval_list):
            lower_limit = interval_list[i]
            upper_limit = interval_list[i + 1]
            if i >= len(interval_list) - 2:
                print(f"The minimum is within a range ({lower_limit}, {upper_limit}")
                plt.plot(lower_limit, fun(lower_limit), 'r|')
                plt.plot(upper_limit, fun(upper_limit), 'r|')
            else:
                print(f"Searched interval is: ( {lower_limit}, {upper_limit})")
                plt.plot(lower_limit, fun(lower_limit), 'g|')
                plt.plot(upper_limit, fun(upper_limit), 'g|')
            i = i + 2

        #plt.plot(x_min - delta, y_min1, 'r|')
        #plt.plot(x_min + delta, y_min2, 'r|')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Minimum')

        plt.show()

