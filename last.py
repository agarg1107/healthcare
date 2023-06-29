# from tkcalendar import Calendar, DateEntry
# try:
#     import tkinter as tk
#     from tkinter import ttk
# except ImportError:
#     import Tkinter as tk
#     import ttk
#
# import datetime
#  # year, month, day
#
# root = tk.Tk()
#
# def get_d():
#     diff21 = (d2 - d1).days
#
# ttk.Label(root, text='Choose date').pack(padx=10, pady=10)
#
# cal = DateEntry(root, width=12, background='red',
#                     foreground='white', borderwidth=2, year=2023)
# cal.pack(padx=10, pady=10)
# selected_date = cal.get_date()
# year = selected_date.year
# month = selected_date.month
# day = selected_date.day
# d1 = datetime.date(year,month,day)
# d2 = datetime.date(2023, 6, 27)
# diff21 = (d2-d1).days
# print(diff21)
# print(str(cal.get()))
#
#
#
#
# root.mainloop()
from CTkMessagebox import CTkMessagebox
import customtkinter


def show_info():
	# Default messagebox for showing some information
	CTkMessagebox(title="Info", message="This is a CTkMessagebox!")


def show_checkmark():
	# Show some positive message with the checkmark icon
	CTkMessagebox(message="CTkMessagebox is successfully installed.",
				  icon="check", option_1="Thanks")


def show_error():
	# Show some error message
	CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")


def show_warning():
	# Show some retry/cancel warnings
	msg = CTkMessagebox(title="Warning Message!", message="Unable to connect!",
						icon="warning", option_1="Cancel", option_2="Retry")

	if msg.get() == "Retry":
		show_warning()


def ask_question():
	# get yes/no answers
	msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
						icon="question", option_1="Cancel", option_2="No", option_3="Yes")
	response = msg.get()

	if response == "Yes":
		app.destroy()
	else:
		print("Click 'Yes' to exit!")


app = customtkinter.CTk()
app.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
app.columnconfigure(0, weight=1)
app.minsize(200, 250)

customtkinter.CTkLabel(app, text="CTk Messagebox Examples").grid(padx=20)
customtkinter.CTkButton(app, text="Check CTkMessagebox", command=show_checkmark).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Info", command=show_info).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Error", command=show_error).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Warning", command=show_warning).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Ask Question", command=ask_question).grid(padx=20, pady=(10, 20), sticky="news")

app.mainloop()
