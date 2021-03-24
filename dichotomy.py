from Equation import Expression
import matplotlib.pyplot as plt

def stepFun(a, b, delta):
    x0 = (a + b) / 2
    x1 = x0 - delta / 2
    x2 = x0 + delta / 2
    return x0, x1, x2

def dichoFun(fun, a, b, delta, it_limit):
    # |------|---|---|------|
    # A    x0-d  x0 x0+d    B

    x0, x1, x2 = stepFun(a, b, delta)
    iterations = 0

    while (a + b) / 2 < delta and iterations <= it_limit:
        iterations = iterations + 1

        if fun(x1) < fun(x2):
            b = x0
            x0, x1, x2 = stepFun(a, b, delta)

        elif fun(x1) > fun(x2):
            a = x0
            x0, x1, x2 = stepFun(a, b, delta)