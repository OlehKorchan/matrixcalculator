from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Menu
from tkinter import ttk
import numpy as np
import tkinter.scrolledtext as tkst
root = Tk()
root.title("Matrix calculator")
root.minsize(800, 600)
root.resizable(width=False, height=False)

def autorinfo():
	sec = Tk()
	sec.title("Info about Autor")
	sec.minsize(200, 200)
	sec.resizable(width=False, height=False)
	info1 = Label(sec, text="\
	\nIdea        Oleh Korchan \
	\nDevelopment Oleh Korchan \
	\nMaintenance Oleh Korchan \
	\nContacts: \
	\ne-mail - olehkorchan@gmail.com \
	\nphone - +380999456034", 
		justify=LEFT)
	info1.grid(row=0, column=0)
def HowToUse():
	sec = Tk()
	sec.title("Instruction")
	sec.minsize(400, 400)
	sec.resizable(width=False, height=False)
	info2 = Label(sec, text=
	 "1) Выберите операцию для матриц и их размерность \
	 \n \n 2) Если вам нужно найти определитель, \
	  \n      то введите искомую матрицу в поле для первой матрицы , \
	  \n      а если возвести матрицу в степень то введите искомую матрицу в поле для первой,\
	  \n      а степень в первую строку и первыый столбец поля второй матрицы. \
	  \n      При этом возводимая матрица должна быть квадратной\
	 \n \n 3) Если вы выбрали операцию умножения матриц, то количество столбцов \
	  \n      первой матрицы должно совпадать с количеством столбцов второй \
	 \n \n 4) Для нахождения суммы или разности матриц вы должны ввести \
	 \n       матрицы одинаковой размерности \
	 \n \n 5) Чтобы 'разделить' матрицы нужно учитывать условие умножения \
	 \n \n 6) Нажмите на кнопку 'Execute' чтобы посчитать результат \
	 \n \n 7) Чтобы выполнить новую операцию нажмите 'Clear' и повторите действия начиная с п. 1",
	 justify=LEFT)
	info2.grid(row=0, column=0) 
menu = Menu(root)
menu.add_command(label='Instruction', command=HowToUse)
root.config(menu=menu)
menu.add_command(label='Autor', command=autorinfo)

combo = Combobox(root)  
combo['values'] = ("SUM", "MINUS", "MULT", "DIV", "POW", "DET")  
combo.current(2)  
combo.grid(row=0,column=0)
#chek = Label(root, text="Rows and colls")
#chek.grid(row=1, column=0)
r1 = Label(root, text="Rows1", justify=LEFT)
r1.grid(row=2, column = 0)
rows1 = Spinbox(root, from_=2, to=20, width=3)  
rows1.grid(column=1, row=2) 
c1 = Label(root, text="Columns1", justify=LEFT)
c1.grid(row=3, column = 0)
colls1 = Spinbox(root, from_=2, to=20, width=3)  
colls1.grid(column=1, row=3) 
r2 = Label(root, text="Rows2", justify=LEFT)
r2.grid(row=4, column = 0)
rows2 = Spinbox(root, from_=2, to=20, width=3)  
rows2.grid(column=1, row=4) 
c1 = Label(root, text="Columns2", justify=LEFT)
c1.grid(row=5, column = 0)
colls2 = Spinbox(root, from_=2, to=20, width=3)  
colls2.grid(column=1, row=5) 

def do():
	global First 
	First = Label(root, text="First Mat")
	First.grid(row=1, column=1)
	global height1 
	height1 = int(rows1.get())
	global width1 
	width1 = int(colls1.get())

	global firstMatrix
	firstMatrix = [[0] * width1 for i in range(height1)]
	for i in range(height1):
		for j in range(width1):
			firstMatrix[i][j] = Entry(root, width=3)
			firstMatrix[i][j].insert(0, "0")
			firstMatrix[i][j].grid(row=i+1, column=j+3)
	global Second 
	Second = Label(root, text="Second Mat")
	Second.grid(row=1, column=width1+3)

	global height2
	height2 = int(rows2.get())
	global width2 
	width2 = int(colls2.get())

	global secondMatrix 
	secondMatrix = [[0] * width2 for i in range(height2)]
	for i in range(height2):
		for j in range(width2):
			secondMatrix[i][j] = Entry(root, width=3)
			secondMatrix[i][j].insert(0, "0")
			secondMatrix[i][j].grid(row=i+1, column=j+width1+4)

def clear():
	for i in range(height1):
		for j in range(width1):
			firstMatrix[i][j].grid_remove()
	for i in range(height2):
		for j in range(width2):
			secondMatrix[i][j].grid_remove()
	First['text'] = ""
	Second['text'] = ""

clir = Button(root, text="Clear", command=clear, width=7, bg="silver")
clir.grid(row=8, column=0)

let = Button(root, text="Create", command=do, width=7, bg="silver")
let.grid(row=9, column=0)

def handler():
	global select 
	select = combo.get()
	if select == "MULT":	
		if width1 != height2:
			output.insert(1.0, "Wrong Matrix's")
			return
		res = [[0] * width2 for i in range(height1)]
		for i in range(height1):
			for j in range(width2):
				for k in range(width1):
					res[i][j] += int(firstMatrix[i][k].get()) * int(secondMatrix[k][j].get())
		for i in range(height1):
			for j in range(width2):
				output.insert(INSERT, '{:>5}'.format(str(res[i][j])))
				#output.insert(INSERT, " ")
			output.insert(INSERT, '\n')
	elif select == "SUM":
		if width1 != width2 or height1 != height2:
			output.insert(1.0, "Wrong Matrix's")
			return
		res = [[0] * width2 for i in range(height1)]
		for i in range(height1):
			for j in range(width2):
				res[i][j] += int(firstMatrix[i][j].get()) + int(secondMatrix[i][j].get())
		for i in range(height1):
			for j in range(width2):
				output.insert(INSERT, '{:>5}'.format(str(res[i][j])))
				#output.insert(INSERT, " ")
			output.insert(INSERT, '\n')
	elif select == "MINUS":
		if width1 != width2 or height1 != height2:
			output.insert(1.0, "Wrong Matrix's")
			return
		res = [[0] * width2 for i in range(height1)]
		for i in range(height1):
			for j in range(width2):
				res[i][j] += int(firstMatrix[i][j].get()) - int(secondMatrix[i][j].get())
		for i in range(height1):
			for j in range(width2):
				output.insert(INSERT, '{:>5}'.format(str(res[i][j])))
				#output.insert(INSERT, " ")
			output.insert(INSERT, '\n')
	elif select == "POW":
		if height1 != width1:
			output.insert(1.0, "Wrong Matrix")
			return
		res = [[0] * width1 for i in range(height1)]
		for i in range(height1):
			for j in range(width1):
				res[i][j] += int(firstMatrix[i][j].get())
		res = np.linalg.matrix_power(res, int(secondMatrix[0][0].get()))
		for i in range(height1):
			for j in range(width1):
				output.insert(INSERT, '{:>5}'.format(str(res[i][j])))
				#output.insert(INSERT, " ")
			output.insert(INSERT, '\n')
	elif select == "DET":
		res = [[0] * width1 for i in range(height1)]
		for i in range(height1):
			for j in range(width1):
				res[i][j] += int(firstMatrix[i][j].get())
		res = np.linalg.det(res)
		output.insert(INSERT, '{:>5}'.format(str(int(res[i][j]))))
		#output.insert(INSERT, " ")
		output.insert(INSERT, '\n')
	elif select == "DIV":
		if width1 != height2:
			output.insert(1.0, "Wrong Matrix's")
			return
		res1 = [[0] * width1 for i in range(height1)]
		for i in range(height1):
			for j in range(width1):
				res1[i][j] += int(firstMatrix[i][j].get())
		res2 = [[0] * width2 for i in range(height2)]
		for i in range(height2):
			for j in range(width2):
				res2[i][j] += int(secondMatrix[i][j].get())
		if np.linalg.det(res2) == 0:
			output.insert(1.0, "Wrong Matrix's")
			return
		res2 = np.linalg.inv(res2)
		some = np.dot(res1, res2)
		for i in range(height1):
			for j in range(width2):
				output.insert(INSERT, '{:>5}'.format(str(some[i][j])))
				#output.insert(INSERT, " ")
			output.insert(INSERT, '\n')
def cleartext():
	output.delete(1.0, END)

but = Button(root, text="Execute",command=handler, width=7, bg="silver").grid(row=7,column=0)
cleartext = Button(root, text="ClearText", command=cleartext, width=7, bg="silver").grid(row=10, column=0)
output = tkst.ScrolledText(root, bg="lightblue", font="Arial 12", width=100, height=10)
output.grid(row=27,column=0, columnspan=50)

root.mainloop()

