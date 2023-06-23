import tkinter as tk
from tkinter import ttk

def get_all_data():
    for item in treeview.get_children():
        values = treeview.item(item)["values"]
        print(values)

# Create the GUI window
window = tk.Tk()

# Create the Treeview
treeview = ttk.Treeview(window)
treeview.pack()

# Insert data into the Treeview
treeview.insert("", "end", values=("Item 1", "Value 1"))
treeview.insert("", "end", values=("Item 2", "Value 2"))

# Create a button to retrieve all data
button = ttk.Button(window, text="Get All Data", command=get_all_data)
button.pack()

# Start the GUI event loop
window.mainloop()
