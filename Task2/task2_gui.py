from tkinter import *
from tkinter import messagebox
from Equation import Expression
from dfp import dfp
 
 
window = Tk()
 
window.title("Task 2")
window.minsize(600,100)
 
def run():
    fields_not_empty  = epsilon.get() and x.get() and y.get() and iterations.get()
    # f = eval(function.get())
    # print(f, epsilon.get(),x.get(), y.get(), iterations.get())
    if fields_not_empty:
        dfp(float(x.get()),float(y.get()),int(iterations.get()),float(epsilon.get()), float(penalty.get()))
    else:
        messagebox.showerror("Error!", "Failure! At Least one of the entries is empty!")

############1st column FUNCTION AND EPSILON##############
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
lower_limit_label = Label(window, width=15,text = "x")
lower_limit_label.grid(column = 1, row =  0, padx=(30,10))

x = StringVar()
lower_limit_entry = Entry(window, width = 15, textvariable = x)
lower_limit_entry.grid(column = 1, row = 1, padx=(30,10))


upper_limit_label = Label(window, width=15,text = "y")
upper_limit_label.grid(column = 1, row =  2, padx=(30,10))

y = StringVar()
upper_limit_entry = Entry(window, width = 15, textvariable = y)
upper_limit_entry.grid(column = 1, row = 3,padx=(30,10))





################### 3RD COLUMN RADIO AND ITERATIONS###############################
iteration_limit_label = Label(window, width=15,text = "Limit of iterations")
iteration_limit_label.grid(column = 2, row =  0, padx=(30,10))

iterations = StringVar()
iteration_limit = Entry(window, width = 15, textvariable = iterations)
iteration_limit.grid(column = 2, row = 1, padx=(30,10))



###################PENALTY COEFFICIENT###############################
penalty_coefficient_label = Label(window, width=15,text = "Penalty Coefficient")
penalty_coefficient_label.grid(column = 2, row =  2, padx=(30,10))

penalty = StringVar()
penalty_entry = Entry(window, width = 15, textvariable = penalty)
penalty_entry.grid(column = 2, row = 3, padx=(30,10))









#Run program
button = Button(window, text = "Run", command = run)
button.grid(column= 3, row = 2, padx=(30,10))
 
window.mainloop()