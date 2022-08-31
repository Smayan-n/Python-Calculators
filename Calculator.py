from tkinter import *
from  tkinter import  messagebox
from tkinter import font as tkFont
import math, os

root = Tk()
root.title("calculator")
root.geometry('354x451')
root.resizable(False, False) 
##################################################

txtFont = tkFont.Font(family='airel', size=26, weight='bold')
txtFont2 = tkFont.Font(family='airel', size=12, weight='bold')

content = StringVar()
currentExpression = StringVar()
expression = ''
ans = 0

pi = math.pi

def error():
	messagebox.showinfo("ERROR", message = "Invalid Calculation")


def calc(num):
	global expression, ans

	expression += str(num)
	content.set(expression)

	
def calculate():
	global expression, ans


	try:
		ans = eval(expression)
		ans = round(ans, 3)

		currentExpression.set(expression)

		expression = str(ans)

		content.set(ans)
		
	except:
		error()
		expression = ''
		ans = 0
		content.set('')
		currentExpression.set('')
		


def clear():
	global expression, ans

	expression = ''
	ans = 0
	content.set('')
	currentExpression.set('')

def backSpace():
	global expression, ans

	if expression != '':

		indChars = []
		indChars[:] = expression
		
		indChars.pop(len(indChars) - 1)

		expression = ''

		for num in indChars:
			expression += str(num)
		
		content.set(expression)

	else:
		currentExpression.set('')

def quad():
	os.system('Quadratic_calculator.py')

#for showing current equations
txtDisp = Entry(root, width=23, state=DISABLED, textvariable = currentExpression, font = txtFont2)
txtDisp.place(x = 4, y = 2)

txtMain = Entry(root, width=18, state=DISABLED, textvariable = content, font = txtFont)
txtMain.place(x = 4, y = 28)


btn7 = Button(root, text = '7', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(7))
btn7.place(x = 0, y = 80)
#y incriments by 93 every 3

btn8 = Button(root, text = '8', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(8))
btn8.place(x = 60, y = 80)

btn9 = Button(root, text = '9', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(9))
btn9.place(x = 120, y = 80)

btn4 = Button(root, text = '4', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(4))
btn4.place(x = 0, y = 173)

btn5 = Button(root, text = '5', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(5))
btn5.place(x = 60, y = 173)

btn6 = Button(root, text = '6', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(6))
btn6.place(x = 120, y = 173)

btn1 = Button(root, text = '1', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(1))
btn1.place(x = 0, y = 266)

btn2 = Button(root, text = '2', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(2))
btn2.place(x = 60, y = 266)

btn3 = Button(root, text = '3', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(3))
btn3.place(x = 120, y = 266)

btn0 = Button(root, text = '0', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc(0))
btn0.place(x = 0, y = 359)

btnDot = Button(root, text = '•', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('.'))
btnDot.place(x = 60, y = 359)

btnPi = Button(root, text = 'quadratic\n calc', bd = 5, fg = 'blue', width = 6, height = 5, command = quad)
btnPi.place(x = 120, y = 359)


btnMult = Button(root, text = '✱', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('*'))
btnMult.place(x = 180, y = 80)

btnDiv = Button(root, text = '/', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('/'))
btnDiv.place(x = 180, y = 173)

btnAdd = Button(root, text = '+', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('+'))
btnAdd.place(x = 180, y = 266)

btnSub = Button(root, text = '-', bd = 5, fg = 'blue', width = 6, height = 5, command = lambda : calc('-'))
btnSub.place(x = 180, y = 359)

btnOpenBr = Button(root, text = '(', bd = 5, fg = 'green', width = 6, height = 5, command = lambda : calc('('))
btnOpenBr.place(x = 240, y = 80)

btnCloseBr = Button(root, text = ')', bd = 5, fg = 'green', width = 6, height = 5, command = lambda : calc(')'))
btnCloseBr.place(x = 296, y = 80)


btnBack = Button(root, text = 'Backspace', bd = 5, fg = 'red', width = 14, height = 5, command = backSpace)
btnBack.place(x = 240, y = 173)

btnClr = Button(root, text = 'Clear', bd = 5, fg = 'red', width = 14, height = 5, command = clear)
btnClr.place(x = 240, y = 266)


btnEqual = Button(root, text = '=', bd = 5, fg = 'green', width = 14, height = 5, command = calculate)
btnEqual.place(x = 240, y = 359)



root.mainloop()









