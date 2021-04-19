from tkinter import *
from tkinter import messagebox
from bisection import draw_bisection
from dichotomy import draw_dichotomy
from Equation import Expression

 
 
window = Tk()
 
window.title("Task 1 - Ruciński & Moszczyński")
window.minsize(600,100)
 
def run():
    fields_not_empty  = function.get() and epsilon.get() and  method.get() and upper_limit.get() and lower_limit.get() and iterations.get()
    print(function.get())
    fun = Expression(function.get(),["x"])

    if method.get() == "bisection" and fields_not_empty:
        draw_bisection(fun,int(lower_limit.get()), int(upper_limit.get()), float(epsilon.get()), int(iterations.get()))
    elif method.get() =="dichotomy" and fields_not_empty:
        draw_dichotomy(fun, int(lower_limit.get()), int(upper_limit.get()), float(epsilon.get()), int(iterations.get()))
    else:
        messagebox.showerror("Error!", "Failure! At Least one of the entries is empty!")



#################1st column FUNCTION AND EPSILON################################
function_label = Label(window, width=15,text = "Function")
function_label.grid(column = 0, row =  0, padx=(30,10))

function = StringVar()
function_entry = Entry(window, width = 15, textvariable = function)
function_entry.grid(column = 0, row =  1, padx=(30,10))

epsilon_label = Label(window, width=15,text = "Epsilon")
epsilon_label.grid(column = 0, row =  2, padx=(30,10))
epsilon_label.configure(text= 'Epsilon')

epsilon = StringVar()
epsilon_entry = Entry(window, width = 15, textvariable = epsilon)
epsilon_entry.grid(column = 0, row = 3, padx=(30,10))







#################2nd column UPPER AND LOWER limits################################
lower_limit_label = Label(window, width=15,text = "Lower limit")
lower_limit_label.grid(column = 1, row =  0, padx=(30,10))

lower_limit = StringVar()
lower_limit_entry = Entry(window, width = 15, textvariable = lower_limit)
lower_limit_entry.grid(column = 1, row = 1, padx=(30,10))


upper_limit_label = Label(window, width=15,text = "Upper limit")
upper_limit_label.grid(column = 1, row =  2, padx=(30,10))

upper_limit = StringVar()
upper_limit_entry = Entry(window, width = 15, textvariable = upper_limit)
upper_limit_entry.grid(column = 1, row = 3,padx=(30,10))





################### 3RD COLUMN RADIO AND ITERATIONS###############################
iteration_limit_label = Label(window, width=15,text = "Limit of iterations")
iteration_limit_label.grid(column = 2, row =  0, padx=(30,10))

iterations = StringVar()
iteration_limit = Entry(window, width = 15, textvariable = iterations)
iteration_limit.grid(column = 2, row = 1, padx=(30,10))

method = StringVar()
radio_1 = Radiobutton(window, text = 'Bisection method',variable=method, value="bisection")
radio_2 = Radiobutton(window, text = 'Dichotomous search', variable=method, value="dichotomy")
radio_1.grid(column= 2, row = 2, padx=(30,10))
radio_2.grid(column= 2, row = 3, padx=(45,10))

#Run program
button = Button(window, text = "Run", command = run)
button.grid(column= 3, row = 2, padx=(30,10))
 
window.mainloop()