#Võ Công Đạt - 43.01.104.021
from tkinter import *
def randnum(event):
	import random
	tx1=tx_1.get();
	tx2=tx_2.get();
	value =random.randint(int(tx1),int(tx2))
	print(value)
	updateDisplay(value)
	
def updateDisplay(myString):
	displayVariable.set(myString)

root=Tk()
root.geometry("300x150")
root.title("App Random")
root.grid()
lbl1=Label(root,text="Nhập Min",font=("TimeNewRoman",12))
lbl1.pack()
tx_1= Entry(root,width=15,font=("TimeNewRoman",12))
tx_1.pack()
lbl2=Label(root,text="Nhập Max",font=("TimeNewRoman",12))
lbl2.pack()
tx_2= Entry(root,width=15,font=("TimeNewRoman",12))
tx_2.pack()
button_1 = Button(root,text="RanDom", font=("TimeNewRoman",14,"bold"),bg="cyan",fg="red") 
button_1.bind("<Button-1>",randnum)
button_1.pack()
displayVariable = StringVar()
displayLabel = Label(root, textvariable=displayVariable)
displayLabel.pack()
root.mainloop()
