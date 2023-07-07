from tkinter import *
import tkinter as tk
root= Tk()
root.geometry("700x250") 


root.title ("Grocery List")
a = Label(root, text="Add or remove items:")
a.pack()
my_entry = Entry(root)
my_entry.pack()

b = Label(root, text = "Price:")
b.pack()
my_entry2=Entry(root)
my_entry2.pack()
def add():
     Listbox.insert(1, my_entry.get().split(" "))
     
def delete_item():
     Listbox.delete(1)


button_frame = Frame(root)

add_button = Button(root, text="Add", width=15, command=add)
add_button.pack()

b2 = Button(root, text = "Remove", width= 15, command=delete_item)
b2.pack()

b3= Button(root, text= "Exit", width=15, command= root.destroy)
b3.pack()

Listbox= Listbox(root)
Listbox.pack()



root.mainloop()
