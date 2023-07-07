# locked in
from tkinter import *

root= Tk()
root.title ("Grocery List")
root.geometry("450x700+500+200")
root.resizable(False, True)
# Trying Treeview for columns

from tkinter import ttk
my_tree= ttk.Treeview(root)
# Defining the columns
my_tree['columns']= ("Item", "Price", "Quantity")
my_tree.column("#0",width= 120, minwidth= 25)
my_tree.column("Item", anchor= W, width= 120)
my_tree.column("Price", anchor= CENTER, width= 120)
my_tree.column("Quantity", anchor= W, width=120)

# Column Headings
my_tree.heading("#0", text= "Label", anchor= W)
my_tree.heading("Item", name= "Item", anchor= W)
my_tree.heading("Price", name= "Price", anchor= CENTER)
my_tree.heading("Quantity", name= "Quantity", anchor=W)

 # Data
my_tree.insert(parent='', index='end',iid= 0, text="Parent", values= ("Kiwi", 1.99, 2) )
my_tree.pack(pady= 20)

# Labels and Buttons
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
add_button = Button(root, text="Add", width=15, command=add)
add_button.pack()

def delete_item():
     Listbox.delete(1)
b2 = Button(root, text = "Remove", width= 15, command=delete_item)
b2.pack()

b3= Button(root, text= "Exit", width=15, command= root.destroy)
b3.pack()

# Listbox
Listbox= Listbox(root)
Listbox.pack()


root.mainloop()


# locked in

