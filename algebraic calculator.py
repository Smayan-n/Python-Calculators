from tkinter import *
from tkinter import *
from  tkinter import  messagebox
from tkinter import font as tkFont
from tkinter import ttk
import math, os
import sympy
from sympy import symbols, Eq, solve, sympify, simplify

root = Tk()
root.title("algebraic eq calc")
root.geometry('420x451')
root.resizable(False, False) 
##################################################

txtFont = tkFont.Font(family='airel', size=26, weight='bold')
txtFont2 = tkFont.Font(family='airel', size=12, weight='bold')
txtFont3 = tkFont.Font(family='airel', size=14, weight='bold')
txtFont4 = tkFont.Font(family='airel', size=17, weight='bold')

content = StringVar()
content2 = StringVar()
dispAns = StringVar()
varDisp = StringVar()
defOpt = StringVar()
defOpt2 = StringVar()
defOpt.set('x')
defOpt2.set("algebraic eq")
varDisp.set('Ans =')
expression = ''
ans = 0
equalVal = ''
selected = True

simplifyMethod = False
algebraicMethod = True

pi = math.pi

x, y = symbols('x y')

def error():
	messagebox.showinfo("ERROR", message = "Invalid Calculation")


def calc(num):
	global expression, ans, equalVal
	if num == '√':
		pass

	if selected:
		expression = txtMain.get()
		expression += str(num)
		content.set(expression)
		
		cursorPos1 = len(expression)
		txtMain.icursor(cursorPos1)

	else:
		equalVal = txtMain2.get()
		equalVal += str(num)
		content2.set(equalVal)
		
		cursorPos2 = len(equalVal)
		txtMain2.icursor(cursorPos2)

	
def calculate():
	global expression, ans, x, y, algebraicMethod, simplifyMethod


	try:
		if algebraicMethod:
			entry1 = txtMain.get()
			entry2 = txtMain2.get()
						
			equation = entry1 + '=' + entry2

			equation = sympify("Eq(" + equation.replace("=", ",") + ")")
						
			ans = solve(equation, solveChoose.get())

			list_check = isinstance(ans, list)
			if list_check:
				if len(ans) == 1:
						ans = str(ans[0]) 
				else:
					ans = str(ans[0]) + ', ' + str(ans[1])
				
			else:
				ans = ans

			dispAns.set(ans)

			if solveChoose.get() == 'x':
				varDisp.set('X = ')
			else:
				varDisp.set('Y = ')

		elif simplifyMethod:
			entry1 = txtMain.get()
			
			equation = sympify(entry1)

			ans = equation.simplify()

			dispAns.set(ans)
		

	except:
		error()
		dispAns.set('')


def clear():
	global expression, ans

	ans = 0
	content.set('')
	content2.set('')
	dispAns.set('')
	varDisp.set("Ans =")


def simplify():
	global simplifyMethod, algebraicMethod
	
	simplifyMethod = True
	algebraicMethod = False

	txtMain2.config(state = DISABLED)
	equalSign.config(state = DISABLED)

	
	content2.set('')
	dispAns.set('')
	varDisp.set("Ans =")



def algebraicEq():
	global simplifyMethod, algebraicMethod
	simplifyMethod = False
	algebraicMethod = True

	txtMain2.config(state = NORMAL)
	equalSign.config(state = NORMAL)

	content2.set('')
	dispAns.set('')
	varDisp.set("Ans =")




ansOutLbl = Label(root, textvariable = varDisp, font = txtFont4)
ansOutLbl.place(x = 0, y = 390)

ansOut = Entry(root, width=26,  textvariable = dispAns, font = txtFont4, state = 'disabled')
ansOut.place(x = 68, y = 390)


txtMain = Entry(root, width=12, textvariable = content, font = txtFont)
txtMain.place(x = 4, y = 20)

equalSign = Label(root, text = '=', font = txtFont)
equalSign.place(x = 245, y = 20)

txtMain2 = Entry(root, width=7, textvariable = content2, font = txtFont)
txtMain2.place(x = 280, y = 20)



btnMult = Button(root, text = '✱', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('*'))
btnMult.place(x = 0, y = 80)

btnDiv = Button(root, text = '/', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('/'))
btnDiv.place(x = 60, y = 80)

btnAdd = Button(root, text = '+', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('+'))
btnAdd.place(x = 120, y = 80)

btnSub = Button(root, text = '-', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('-'))
btnSub.place(x = 180, y = 80)

btnSquare = Button(root, text = 'a^\n (power)', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('**'))
btnSquare.place(x = 0, y = 173)

btnSqrt = Button(root, text = '√\n (sqrt)', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('√'))
btnSqrt.place(x = 60, y = 173)



btnOpenBr = Button(root, text = '(', bd = 5, fg = 'green', width = 6, height = 5, command = lambda : calc('('))
btnOpenBr.place(x = 240, y = 80)

btnCloseBr = Button(root, text = ')', bd = 5, fg = 'green', width = 6, height = 5, command = lambda : calc(')'))
btnCloseBr.place(x = 296, y = 80)

x = Button(root, text = 'X', bd = 5, fg = 'green', width = 6, height = 5, command = lambda : calc('x'))
x.place(x = 240, y = 173)

y = Button(root, text = 'Y', bd = 5, fg = 'green', width = 6, height = 5, command = lambda : calc('y'))
y.place(x = 296, y = 173)


btnClr = Button(root, text = 'Clear', bd = 5, fg = 'red', width = 7, height = 11, command = clear)
btnClr.place(x = 355, y = 82)


btnEqual = Button(root, text = '=', bd = 5, fg = 'green', width = 23, height = 5, command = calculate)
btnEqual.place(x = 244, y = 265)


solveForTxt = Label(root, text = "Solve For:", font = txtFont3)
solveForTxt.place(x = 122, y = 173)

solveChoose = ttk.Combobox(root, values = ('x', 'y'), height = 8, width = 15,state='readonly', textvariable = defOpt)
solveChoose.place(x = 122, y = 198)


typeTxt = Label(root, text = "Function:", font = txtFont3)
typeTxt.place(x = 122, y = 220)

typeChoose = ttk.Combobox(root, values = ('algebraic eq', 'simplify'), height = 8, width = 15,state='readonly', textvariable = defOpt2)
typeChoose.place(x = 122, y = 250)




def repeat():
	
	if typeChoose.get() == "simplify":
		simplify()
		repeat2()
		return

	
	root.after(100, repeat)

def repeat2():

	if typeChoose.get() == "algebraic eq":
		algebraicEq()
		repeat()
		return


	root.after(100, repeat2)


def selTrue(event):
	global selected
	selected = True

def selFalse(event):
	global selected
	selected = False

txtMain.bind("<FocusIn>", selTrue)
txtMain2.bind("<FocusIn>", selFalse)


repeat2()

root.mainloop()


