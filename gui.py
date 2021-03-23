from tkinter import *
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


 
 
window = Tk()
 
window.title("Task 1 - Ruciński & Moszczyński")
window.minsize(600,400)
 
def clickMe():
    pass

label = Label(window, text = "Function")
label.grid(column = 0, row = 0)
label.configure(text= 'Function')


epsilon_label = Label(window, text = "Enter Function")
epsilon_label.grid(column = 2, row =  0, padx=(50,10))
epsilon_label.configure(text= 'Epsilon')

 
function = StringVar()
nameEntered = Entry(window, width = 15, textvariable = function)
nameEntered.grid(column = 0, row = 1)

epsilon = StringVar()
epsilonEntered = Entry(window, width = 15, textvariable = epsilon)
epsilonEntered.grid(column = 2, row = 1, padx=(50,10))
 
 
button = Button(window, text = "Click Me", command = clickMe)
button.grid(column= 0, row = 2)



# RADIO BUTTONS 

# Tkinter string variable 
# able to store any string value 

radio_1 = Radiobutton(window, text = 'Bisection method')
radio_2 = Radiobutton(window, text = 'Dichotomous search')
radio_1.grid(column= 3, row = 0, padx=(35,10))
radio_2.grid(column= 3, row = 1, padx=(50,10))


f = Figure()

# canvas = FigureCanvasTkAgg(f, master=window)
# canvas.draw()
# canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
# canvas._tkcanvas.grid(column= 3,fill="both", expand=1)


 
window.mainloop()