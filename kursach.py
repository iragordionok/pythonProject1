from tkinter import *
from tkinter import ttk

root = Tk()
root.title("База химических реакций")
root.geometry("640x480")

labelTop = Label(text="Выберете химический элемент")
labelTop.grid(column=0, row=0)

chemical_list = write_elements()
comboExample = ttk.Combobox(values=chemical_list, postcommand=changeelements)
comboExample.grid(column=0, row=1)
comboExample.current(0)
name_el = comboExample.get()

comboExample.bind("<<ComboboxSelected>>", callback)

entry_n1 = ttk.Entry()
entry_n1.grid(column=1, row=1)

btn_change_label = Button(text="Добавить реакцию", command = btn_click)
btn_change_label.grid(column=1, row=2)

btn_change_label1 = Button(text="Показать все реакции", command = btn_click1)
btn_change_label1.grid(column=1, row=3)

text = open('Reactions.txt', encoding='utf-8').readlines()
text = ''.join(text)
textline = Text(root)
textline.insert(1.0, text)
textline.grid(column=3, row=0, rowspan=20)
textline.configure(state = 'disabled')

root.mainloop()