import tkinter as tk
from tkinter import ttk

def get_matching_options(text):
    # Add your logic here to retrieve matching options based on the entered text
    # Return a list of matching options
    # For simplicity, we'll return a static list in this example
    options = ["Apple", "Banana", "Orange", "Pineapple"]
    return [option for option in options if text.lower() in option.lower()]

def on_key_press(event):
    text = combobox.get()
    matching_options = get_matching_options(text)
    combobox['values'] = matching_options
    combobox.event_generate('<<ComboboxSelected>>')  # Trigger drop-down

root = tk.Tk()

combobox = ttk.Combobox(root)
combobox.pack()

combobox.bind('<KeyRelease>', on_key_press)

root.mainloop()
def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add toppings to listbox
    for item in data:
        my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(e):
    my_entry.delete(0, END)
    selected_item = my_list.get(ANCHOR)
    my_entry.insert(0, selected_item)
    my_list.selection_clear(0, END)

# Create function to check entry vs listbox
def check(e):
    # Grab what was typed
    typed = my_entry.get()

    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)

    # Update the listbox with selected items
    update(data)

def bind_code():
    # Create a binding on the listbox onclick
    my_list.bind("<<ListboxSelect>>", fillout)

    # Create a binding on the entry box
    my_entry.bind("<KeyRelease>", check)
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.place(x = 1000 , y = 200)

my_list = Listbox(root, width=50)
my_list.place(x = 1000,y = 400)

# Create a list of pizza toppings
toppings = []
file = openpyxl.load_workbook('Student_data_2.xlsx')
sheet = file.active

for row in sheet.rows:
    toppings.append(row[1].value)

# Add the toppings to our list
update(toppings)
bind_code()