from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import math, keyboard


x = 275
y = 300
root = Tk()
root.minsize(x, y)
root.title("Quadratic Clac")
root.resizable(False, False)
#########################################

txtFont = tkFont.Font(family='airel', size=15, weight='bold')
txtFont2 = tkFont.Font(family='airel', size=14, weight='bold')

x1 = StringVar()
x2 = StringVar()

def solve():
	
	try:
		a = float(entryA.get())
		b = float(entryB.get())
		c = float(entryC.get())

		sqrt_part = math.sqrt(((b)**2)-4*a*c)

		X1 = (((-b)+(sqrt_part))/(2*a))
		X2 = (((-b)-(sqrt_part))/(2*a))

		X1 = round(X1, 5)
		X2 = round(X2, 5)

		x1.set(str(X1))
		x2.set(str(X2))

	except:
		messagebox.showinfo("ERROR", message = "Invalid Calculation")



#box = ttk.Combobox(root, values=["second","third","four"], textvariable = boxvar, state = 'readonly')
#box.place(x= 0, y= 100)


labelInfo = Label(root, text = "ax^2 + bx + c\n solve for x:", font = txtFont)
labelInfo.grid(row = 1, column = 2)


labelA = Label(root, text = "a:", font = txtFont)
labelA.grid(row = 2, column = 1)

entryA = Entry(root, bd = 2, font = txtFont2)
entryA.grid(row = 2, column = 2)

labelB = Label(root, text = "b:", font = txtFont)
labelB.grid(row = 3, column = 1)

entryB = Entry(root, bd = 2, font = txtFont2)
entryB.grid(row = 3, column = 2)

labelC = Label(root, text = "c:", font = txtFont)
labelC.grid(row = 4, column = 1)

entryC = Entry(root, bd = 2, font = txtFont2)
entryC.grid(row = 4, column = 2)


btnSolve = Button(root, fg = 'green', bd = 5, height = 3, width = 14, text = "Solve", command = solve)
btnSolve.grid(row = 5, column = 2)

labelX1 = Label(root, text = "X1:", font = txtFont2)
labelX1.place(x = 1, y = 220)
enryX1 = Entry(root, bd = 2, textvariable = x1, state = DISABLED, font = txtFont2)
enryX1.place(x = 40, y = 220)

labelX2 = Label(root, text = "X2:", font = txtFont2)
labelX2.place(x = 1, y = 260)
enryX2 = Entry(root, bd = 2, textvariable = x2, state = DISABLED, font = txtFont2)
enryX2.place(x = 40, y = 260)

root.mainloop()