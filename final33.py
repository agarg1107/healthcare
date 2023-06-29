# import openpyxl
#
#
# def get_row_values(file_path, sheet_name, row_number, column_indices=None, column_names=None):
#     workbook = openpyxl.load_workbook(file_path)
#     sheet = workbook.active
#     row_values = []
#     for cell in sheet[row_number]:
#         column_index = cell.column
#         column_name = openpyxl.utils.get_column_letter(column_index)
#
#         if column_indices is not None and column_index in column_indices:
#             row_values.append(cell.value)
#         elif column_names is not None and column_name in column_names:
#             row_values.append(cell.value)
#
#     workbook.close()
#
#     return row_values
#
#
# # Usage example
# file_path = 'Stock.xlsx'
# sheet_name = 'Sheet1'
# row_number = 2
# columns = [1, 3, 5]  # Specify column indices (1-based) or column names
#
# values = get_row_values(file_path, sheet_name, row_number, column_indices=columns)
# print(values)

import tkinter as tk
from tkinter import ttk

def get_treeview_data(treeview):
    data = []
    for item in treeview.get_children():
        values = treeview.item(item)['values']
        data.append(values)
    return data

# Create a sample Tkinter window
window = tk.Tk()

# Create a TreeView widget
treeview = ttk.Treeview(window)
treeview['columns'] = ('Name', 'Age')

# Insert data into TreeView
treeview.insert('', 'end', text='1', values=('John Doe', 25))
treeview.insert('', 'end', text='2', values=('Jane Smith', 30))
treeview.insert('', 'end', text='3', values=('Alex Johnson', 40))

# Retrieve data from TreeView
treeview_data = get_treeview_data(treeview)
print(treeview_data)

window.mainloop()
