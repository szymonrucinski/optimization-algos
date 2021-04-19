import numpy as np
import copy
import numdifftools as nd
#http://sms.am.put.poznan.pl/wp-content/uploads/2019/12/POPK_03.pdf
#https://slideplayer.com/slide/4260069/


def fun(xy): 
    return (100*(xy[1]**2 -xy[1]**2)+(1-xy[0]**2))

def gradient(point):
    print(point[0],point[1])
    result = nd.Gradient(fun)([point[0],point[1]])
    return result.reshape(-1,1)

def calculate_lambda():
    pass

def calculate_M(S,step, gradient_diff):
    print(S)
    print(S.transpose())
    M_1 = S.dot(S.transpose())
    M_2 = S.transpose()*gradient_diff
    M = step * np.divide(M_1,M_2)
    return M

def calculate_N(current_hessian_approx, gradient_diff):

    N_1 = current_hessian_approx.dot(gradient_diff)
    N_1 = N_1.dot(N_1.transpose())

    N_2 = gradient_diff.transpose()
    N_2 = N_2.dot(current_hessian_approx)
    N_3 = N_2.dot(gradient_diff)

    print(type(N_1), type(N_3))

    N = np.divide(N_1,N_3)
    return N

#Gradient approximation
def update_hessian_approx(current_hessian_approx,S,next_gradient, current_gradient ,step,delta_x):
    # #Secant equation

    # B = current_hessian_approx
    # A_1 = np.dot(delta_x,delta_x.transpose())
    # # A_2  =np.dot()



    # gradient_diff = np.subtract(next_gradient,current_gradient)
    # M = calculate_M(S,step, gradient_diff)
    # N = calculate_N(current_hessian_approx, gradient_diff)

    # current_hessian_approx = current_hessian_approx + M + N
    # return current_hessian_approx
    return current_hessian_approx + 
  

def new_update():
    p = np.dot(current_hessian_approx,current_gradient)
    d = np.dot(cu)
    # v = p - d
    v = np.divide()


# def find_direction(hessian_approx, grad_m1, grad, step):
#     H = hessian_approx
#     grad_diff = grad - grad_m1
#     ys = np.inner(grad_diff, step)
#     Hy = np.dot(H, grad_diff)
#     yHy = np.inner(grad_diff, Hy)
#     H += (ys + yHy) * np.outer(step, step) / ys ** 2
#     H -= (np.outer(Hy, step) + np.outer(step, Hy)) / ys
#     direction = -np.dot(H, grad)
#     return direction, {'gradient_diff': grad_diff}



def stop_fpd(gradient,epsilon):
    print("stop hatl")
    print(gradient)
    result =  np.absolute(gradient) < epsilon
    return np.any(result, where=[[False], [True]])

def fpd(x,y,it_num,step,lambada):
    #Tego na razie nie wykorzystujemy
    epsilon = 0.5
    alpha = fun([x,y])
    lambada

    #Macierz 2x2 o dodatnim wyznaczniku lub jednostkowa
    hessian_approx = np.identity(2)
    point = np.array([[x,y]],np.float64).transpose()

    for i in range(0,it_num):
        current_gradient = gradient(point)
        #1) Compute approx. Newton , update direction
        # KIERUNEK POPRAWY
        S = -1 * np.dot(hessian_approx, current_gradient)
        #2) Line search (inexact)
        delta_x = point
        print("delta",delta_x)
        point = point - np.dot(lambada,S)
        print("delta after",delta_x)
        delta_x = delta_x - point
        #3) Computer gradient for point x_(i+1)
        next_gradient = gradient(point)
        #4) Update Hessian
        hessian_approx = update_hessian_approx(hessian_approx, S, next_gradient,current_gradient, step, delta_x)
        if stop_fpd(current_gradient, epsilon):
            break

fpd(x = -2, y = -2 ,it_num = 3, step = 1, lambada = 0.2)
