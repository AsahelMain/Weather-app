from tkinter import *
import readcsv

master = Tk()
myTickets = readcsv.getTickets()

variable = StringVar(master)
variable.set(myTickets[1]) # default value

w = OptionMenu(master, variable, *myTickets)
w.pack()

mainloop()