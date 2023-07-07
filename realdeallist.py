from tkinter import *
from tkinter import ttk
root= Tk()
root.title("Grocery List App")
root.geometry("450x700+500+200")
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
my_tree.insert(parent="", index="end",iid= 0, text="Parent", values= ("Kiwi", 1.99, 2) )
my_tree.pack(pady= 20)

root.mainloop()