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
root.iconbitmap('D:/Programming/Ai and Ml/Machine learning tut/healthcare/Student Images/1.jpg')
root.geometry("800x800")

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

	selected_item = my_list.get(ANCHOR)
	my_entry.insert(0, selected_item)

	my_list.selection_clear(0, END)

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





my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()



my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list of pizza toppings
toppings = []
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