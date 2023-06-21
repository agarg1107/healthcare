from tkinter import *

from datetime import date
from tkinter import messagebox
from PIL import Image
from tkinter.ttk import Combobox
import openpyxl
from openpyxl import Workbook
import pathlib
import tkinter as tk
import customtkinter

root = Tk()
root.title('Codemy.com - Auto Select/Search')

root.geometry("500x300")

# Update the listbox
def update(data):
	# Clear the listbox
	my_list.delete(0, END)

	# Add toppings to listbox
	for item in data:
		my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(e):
	my_entry.delete(0, END)

	# Add clicked list item to entry box
	selected_item = my_list.get(ANCHOR)
	my_entry.insert(0, selected_item)

	# Disable the entry box after selection


	# Reset the listbox selection
	my_list.selection_clear(0, END)
	a = my_entry.get()
	for row in sheet.rows:
		if row[1].value == a:
			name = row[0].value
			try:
				print(str(name))
			except:
				messagebox.showerror("Invalid", "Invalid registration number! !!")
	x1 = sheet.cell(row=int(int(name)+1), column=1).value
	print(x1)
	x1 = sheet.cell(row=int(int(name)+1), column=2).value
	print(x1)
	x1 = sheet.cell(row=int(int(name)+1), column=3).value
	print(x1)
	x1 = sheet.cell(row=int(int(name)+1), column=4).value
	print(x1)
	x1 = sheet.cell(row=int(int(name)+1), column=5).value
	print(x1)
	x1 = sheet.cell(row=int(int(name)+1), column=6).value
	print(x1)


# Create function to check entry vs listbox
def check(e):
	# grab what was typed
	typed = my_entry.get()

	if typed == '':
		data = toppings
	else:
		data = []
		for item in toppings:
			if typed.lower() in item.lower():
				data.append(item)

	# update our listbox with selected items
	update(data)

a= ""
name = 0
# Create a label
my_label = Label(root, text="Start Typing...",
	font=("Helvetica", 14), fg="grey")

my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list of pizza toppings
toppings = ["Pepperoni", "Peppers", "Mushrooms",
	"Cheese", "Onions", "Ham", "Taco"]
file = openpyxl.load_workbook('Student_data_2.xlsx')
sheet = file.active

for row in sheet.rows:
	toppings.append(row[1].value)


# Add the toppings to our list
update(toppings)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()