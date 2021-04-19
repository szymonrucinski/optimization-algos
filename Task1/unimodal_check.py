import numpy as np
import math

def is_unimodal(fun,a,b):
    mid_point = (a+b)/2
    step = 0.2
    if fun(a) > fun(mid_point) and fun(b) > fun(mid_point):
        print(f"Function is unimodal in a range: ({a}, {b})")
        return True
    else:
        interval_start = a + step
        interval_end = b - step
        counter = 0
        print(f"Function is not unimodal in range: ({a}, {b})")

        while not (fun(interval_start) > fun(mid_point) and fun(interval_end) > fun(mid_point)) and counter < 50:
            interval_start += step
            interval_end -= step
            counter += 1

        if counter < 50:
            print(f"Function is unimodal in range ({interval_start}, {interval_end})")
        else:
            print("Function doesn't have a local minimum in this interval.")

        return False