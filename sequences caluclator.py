import math
from tkinter import *
from  tkinter import  messagebox




def error(type): #type parameter for displaying only single error
	global outputAns, otherOut


	#setting all output foields to blank
	outputAns.set('')
	otherOut.set('')

	if type == "seq":
		outputAns.set("Error: Invalid sequence")
	elif type == "void":
		outputAns.set("Error: void entry")
	elif type == "min":
		outputAns.set("Error: Enter minimum of 3 values")
	else:
		outputAns.set("Error: Invalid syntax")

#func to make UI
def initUI():
	global outputAns, otherOut

	root = Tk()
	root.title("sequence calcuator")
	root.geometry('550x430')

	#iterable var for output
	outputAns = StringVar()
	otherOut = StringVar()


	#the 2 labeles to ask for input
	enterLbl = Label(root, text = "Enter the first values of your sequence(min 3)", 
					bg = 'aqua', font = ('aerial', 16, 'bold'))
	enterLbl.place(x = 10, y = 0)

	howLbl = Label(root, text = "seperate the values by a comma. example: 3,4,5", 
					bg = 'red', font = ('aerial', 12, 'bold'))
	howLbl.place(x = 10, y = 40)

	#the sequence entry
	Entry1 = Entry(root, width = 30, font = ('airel', 15, 'bold'), bd = 3, bg = 'aqua')
	Entry1.place(x= 10, y=100)

	#next numbers prompt and input
	Entry2Lbl = Label(root, text = "Number of values needed after these:", font = ('aerial', 12, 'bold'), bg = 'orange')
	Entry2Lbl.place(x= 10, y = 160)

	Entry2 = Entry(root, width = 10, font = ('airel', 15, 'bold'), bd = 3, bg = 'orange')
	Entry2.place(x= 10, y=190)

	#button to calculate
	btn = Button(root, text = "calculate!", font = ('aerial', 14, 'bold'), bd = 5,
				command = lambda: getValues(Entry1.get(), Entry2.get())) #calling getvalues func with params when pressed
	btn.place(x = 350, y = 180)


	#output label
	ansLbl = Label(root, text = "Answer:", font = ('aerial', 15, 'bold'), bg = 'pink')
	ansLbl.place(x= 10, y = 250)

	outLbl = Label(root, textvariable = outputAns, font = ('aerial', 15, 'bold'))
	outLbl.place(x= 10, y = 280)


	#other labels for common diff/ratio and seq type
	otherLbl = Label(root, text = "Sequence type:              Common change:", font = ('aerial', 15, 'bold'), bg = 'pink')
	otherLbl.place(x= 10, y = 320)

	otherLbl2 = Label(root, textvariable = otherOut, font = ('aerial', 15, 'bold'))
	otherLbl2.place(x= 10, y = 350)

	root.mainloop()
	


#seperating sequence into individual chars
def getValues(sequence, calcNum):
	#calcnum is the no. of more values after the ones given
	if calcNum == '':
		error("void")
		return None

	sequence_vals = []
	sequence_vals_final = []


	sequence_vals[:] = sequence 

	#filtering out values between commas
	value = ''
	for i, char in enumerate(sequence_vals):
		
		if char == ',':
			sequence_vals_final.append(value)
			value = ''
			
		else:
			value += sequence_vals[i]
			
	sequence_vals_final.append(value)#appending last value stored 
	
	#seeing if min nums input is 3
	if len(sequence_vals_final) < 3:
		error("min")
		return None

	#determining if all vals in list are ints. If not then it must be syntax error
	for val in sequence_vals_final:
		try:
			val = float(val)
		except:
			error("syntax")
			return


	#calling next function .
	calculateType(sequence_vals_final, calcNum)


#calculating wether the seq is geometric or arithmetic
def calculateType(sequence, calcNum):
	global otherOut

	
	differences = []
	ratios = []

	for i in range(len(sequence) - 1):

		#finding both common ratios and differences first
		differences.append(float(sequence[i + 1]) - float(sequence[i]))
		ratios.append(float(sequence[i + 1]) / float(sequence[i]))

	#print(differences, ratios)

	#checking if all differences are the same for all values and for the one which it is, that is they type
	allSameDiff = all(diff == differences[0] for diff in differences)
	allSameRatios = all(ratio == ratios[0] for ratio in ratios)

	#checking if all the common diff/ rarios are the same(for user input or wrong sequences)
	if allSameDiff:
		Type = True
		diff = differences[0]
		otherOut.set("Arithmetic" + "                               +" + str(diff))#giving info on seq too
	elif allSameRatios:
		Type = False
		diff = ratios[0]
		otherOut.set("Geometric" + "                               x" + str(diff))#giving info on seq too
	else:
		error("seq")
		return None #invalid seq if none are same

	

	calculateSequence(Type, sequence, diff, calcNum)

def calculateSequence(Type, sequence, diff, calcNum):
	global outputAns

	output = []
	output.append(float(sequence[0]))

	for i in range(int(calcNum) - 1 + len(sequence)): #calcnum -1 cause otherwise it gives extra value

		if Type: #if true, its arithmetic,if false its geometic
			val = float(output[i]) + diff
		else:
			val = float(output[i]) * diff
		
		output.append(val)


	#setting output
	outStr = ''
	for val in output:
		outStr += str(val) + ",  " #to put output in a readable format

	outputAns.set(outStr)
	


if __name__ == '__main__':
	initUI()#start staement (after this funcs are called from other funcs)