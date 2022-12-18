"""""
import tkinter
from tkinter import *

def writeFile():
    file = open('Reactions.txt','a+')
    file.write(metinF.get() + '\n')
    file.close()

gui = Tk()

metinF = Entry(gui)
metinF.grid(row=9, column=1)

butonWrite = Button(gui)
butonWrite.config(text = 'Write To File', command = writeFile)
butonWrite.grid(row=8, column=1)

gui.mainloop()
"""""



def change():
    mylines = []
    with open('Reactions.txt', 'r') as myfile:
        for myline in myfile:
            mylines.append(myline.rstrip('\n'))
        print(mylines)
        result = "\n".join(mylines)
change()



