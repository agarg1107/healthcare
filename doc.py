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

customtkinter.set_appearance_mode("System")
textcolor = "#333333"
side_frame_col = "#F2DFD7"
buttoncolor = "#FF5722"
buttoncolorlite = "#FF855F"
background = "#D4C1EC"
obj_frame_col = "#9F9FED"
mainbackground = "#736ced"
framebg = "#EDEDED"
framefg = "#06283D"
root = Tk()
maincol1 = "pink"
maincol2 = "pink"
maincol3 = "pink"
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.title("Clinic Managment System")
root.state('zoomed')
# root.geometry ("%dx%d"%(width,height))
root.config(bg=mainbackground)
# pathmain = "//LAPTOP-F1A0LRP8/Users/aman/Student_data.xlsx"
pathmain = "Student_data.xlsx"
file = pathlib.Path(pathmain)

if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active

    sheet['A1'] = "Registration No."
    sheet['B1'] = "Name"
    sheet['C1'] = "Class"
    sheet['D1'] = "Gender"
    sheet['E1'] = "D0B"
    sheet['F1'] = "Date Of Registration"
    sheet['G1'] = "weight"
    sheet['H1'] = "height"
    sheet['I1'] = "Temperature"
    sheet['J1'] = "Respiration"
    sheet['K1'] = "Pulse"
    sheet['L1'] = "BP"
    sheet['M1'] = "Village"
    sheet['N1'] = "Mobile"

    file.save(pathmain)

def update():
    root.after(1000, update)  # run itself again after 1000 ms


def Exit():
    root.destroy()


def registration_no():
    file = openpyxl.load_workbook(pathmain)
    sheet = file.active
    row = sheet.max_row

    max_row_value = sheet.cell(row=row, column=1).value

    try:
        Registration.set(max_row_value + 1)

    except:
        Registration.set("1")


def Clear():
    global img
    Name.set('')
    age.set('')
    weight.set('')
    height.set('')
    temprature.set('')
    respiration.set('')
    pulse.set('')
    bp.set('')
    village.set('')
    mobile.set('')

    registration_no()


def Clear2():
    saveButton.configure(state='active')
    global img
    Name.set('')
    age.set('')
    weight.set('')
    height.set('')
    village.set('')
    mobile.set('')
    temprature.set('')
    respiration.set('')
    pulse.set('')
    bp.set('')

    registration_no()


def Save():

    print("abcd")



def search():
    text = Search.get()  # taking input from entry box

    Clear()  # to clear all the data already available in entry box and other
    saveButton.configure(
        state='disable')  # after clicking on search , save button will disable so that no one can click on

    file = openpyxl.load_workbook(pathmain)
    sheet = file.active

    for row in sheet.rows:
        if row[0].value == int(text):
            name = row[0]
            reg_no_position = str(name)[14:-1]
            reg_number = str(name)[15:-1]
            try:
                print(str(name))
            except:
                messagebox.showerror("Invalid", "Invalid registration number! !!")

    x1 = sheet.cell(row=int(reg_number), column=1).value
    x2 = sheet.cell(row=int(reg_number), column=2).value
    x3 = sheet.cell(row=int(reg_number), column=3).value
    x4 = sheet.cell(row=int(reg_number), column=4).value
    x5 = sheet.cell(row=int(reg_number), column=5).value
    x6 = sheet.cell(row=int(reg_number), column=6).value
    x7 = sheet.cell(row=int(reg_number), column=7).value
    x8 = sheet.cell(row=int(reg_number), column=8).value
    x9 = sheet.cell(row=int(reg_number), column=9).value
    x10 = sheet.cell(row=int(reg_number), column=10).value
    x11 = sheet.cell(row=int(reg_number), column=11).value
    x12 = sheet.cell(row=int(reg_number), column=12).value
    x13 = sheet.cell(row=int(reg_number), column=13).value
    x14 = sheet.cell(row=int(reg_number), column=14).value

    Registration.set(x1)
    Name.set(x2)


    if x4 == "Female":
        Gender.set("Female")

    else:
        Gender.set("male")

    age.set(x5)

    Date.set(x6)

    weight.set(x7)

    height.set(x8)
    temprature.set(x9)

    respiration.set(x10)
    pulse.set(x11)
    bp.set(x12)
    village.set(x13)
    mobile.set(x14)

    ####################################gender#####################################


def selection():
    global gender
    value = radio.get()
    if value == 1:
        gender = "Male"
    else:
        gender = "Female"


fontmain = "Dotum"
Name = StringVar()
age = StringVar()
radio = IntVar()
weight = StringVar()
height = StringVar()
temprature = StringVar()
pulse = StringVar()
respiration = StringVar()
bp = StringVar()
obj = None
mobile = StringVar()
village = StringVar()
Search = StringVar()
Gender = StringVar()
my_list = Listbox
my_entry = Entry

name_lable = customtkinter.CTkLabel

# top frames
obj = customtkinter.CTkFrame(master=root, corner_radius=15, width=400, height=600, fg_color=obj_frame_col, border_width=4,
                             border_color="black")
obj.place(x=230, y=130)
obj2 = customtkinter.CTkFrame(master=root, corner_radius=15, width=850, height=600, fg_color=obj_frame_col, border_width=4,
                             border_color="black")
obj2.place(x=650, y=130)
Label(root, text="Clinic Management", width=10, height=2, bg="#c36464", fg='#fff', font='arial 20 bold').pack(side=TOP,
                                                                                                              fill=X)
# Registration and Date

customtkinter.CTkLabel(master=root, text="Date:", text_color=textcolor,font=(fontmain, 20)).place(x=230, y=77)
Registration = IntVar()
Date = StringVar()


registration_no()

today = date.today()
d1 = today.strftime("%d/%m/%Y")
customtkinter.CTkLabel(root, textvariable=Date, text_color=textcolor, font=(fontmain, 20)).place(x=290, y=75)

Date.set(d1)
# Doctor work



# frame
def reg_page():
    # Labels
    customtkinter.CTkLabel(obj, text="Full Name:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=55)
    customtkinter.CTkLabel(obj, text="Age:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=105)
    customtkinter.CTkLabel(obj, text="Gender:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=155)
    customtkinter.CTkLabel(obj, text="Weight:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=355)
    customtkinter.CTkLabel(obj, text="Height:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=405)
    customtkinter.CTkLabel(obj, text="Temperature:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=205)
    customtkinter.CTkLabel(obj, text="Pulse:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=255)
    customtkinter.CTkLabel(obj, text="Respiration:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=455)
    customtkinter.CTkLabel(obj, text="BP:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=505)
    customtkinter.CTkLabel(obj, text="Village Name:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=305)
    customtkinter.CTkLabel(obj, text="Mobile:", text_color=textcolor,font=(fontmain, 20)).place(x=30, y=555)

    # Entry
    customtkinter.CTkLabel(obj, textvariable = Name, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=50)
    customtkinter.CTkLabel(obj, textvariable = age, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=100)
    customtkinter.CTkLabel(obj, textvariable = weight, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=350)
    customtkinter.CTkLabel(obj, textvariable = height, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=400)
    customtkinter.CTkLabel(obj, textvariable = temprature, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=200)
    customtkinter.CTkLabel(obj, textvariable = pulse, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=250)
    customtkinter.CTkLabel(obj, textvariable = respiration, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=450)
    customtkinter.CTkLabel(obj, textvariable = bp, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=500)
    customtkinter.CTkLabel(obj, textvariable = village, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=550)
    customtkinter.CTkLabel(obj, textvariable = mobile, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=300)
    customtkinter.CTkLabel(obj, textvariable= Gender, text_color=textcolor, font=(fontmain, 20)).place(x=170, y=160)

    # Doc
    textbox = customtkinter.CTkTextbox(obj2, fg_color="white", width=400, height=200).place(x=400, y=50)





def stock_page():
    s_p = tk.Frame(obj)
    tk.Label(s_p, text='stock Page\n\nPage:3', font='Bold,30').place(x=1,y=1)


def del_page():
    for frame in obj.winfo_children():
        frame.destroy()
    for frame in obj2.winfo_children():
        frame.destroy()


def hideindicate():
    reg_indicate.config(bg=buttoncolorlite)

    stock_indicate.config(bg=buttoncolorlite)

    reg_btn.configure(fg_color=buttoncolorlite)

    stock_btn.configure(fg_color=buttoncolorlite)


def indicate(lb, btn, page):
    hideindicate()
    if btn == 1:
        reg_btn.configure(fg_color=buttoncolor)
    else:
        stock_btn.configure(fg_color=buttoncolor)
    lb.config(bg=buttoncolor)
    del_page()
    page()

reg_page()
option_frame = customtkinter.CTkFrame(master=root, corner_radius=0, fg_color=side_frame_col)
my_image = customtkinter.CTkImage(light_image=Image.open("stock-removebg-preview.png"),
                                  dark_image=Image.open("stock-removebg-preview.png"),
                                  size=(40, 40))
reg_btn = customtkinter.CTkButton(option_frame, image=my_image, fg_color=buttoncolor, hover="disable", text='Check-Up',
                                  width=150, corner_radius=10, border_width=2, border_color="black", border_spacing=2,
                                  height=40, command=lambda: indicate(reg_indicate, 1, reg_page))
reg_btn.place(x=15, y=50)

reg_indicate = tk.Label(option_frame, text='', bg=buttoncolor)
reg_indicate.place(x=3, y=55, width=5, height=40)


stock_btn = customtkinter.CTkButton(option_frame, text='Stock            ', hover="disable", image=my_image,
                                    fg_color=buttoncolorlite, width=150, corner_radius=10, border_width=2,
                                    border_color="black", border_spacing=2, height=40,
                                    command=lambda: indicate(stock_indicate, 3, stock_page))
stock_btn.place(x=15, y=160)

stock_indicate = tk.Label(option_frame, text='', bg=buttoncolor)
stock_indicate.place(x=3, y=165, width=5, height=40)

option_frame.pack(side=tk.LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=200, height=730)
main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=10)

# button


customtkinter.CTkEntry(master=root, corner_radius=15,text_color=textcolor, fg_color=background,textvariable=Search, placeholder_text="search", height=40,
                       font=(fontmain, 20), width=220).place(x=1110, y=75)
imageicon3 = PhotoImage(file="Images/search.png")
srchimage = customtkinter.CTkImage(light_image=Image.open("stock-removebg-preview.png"),
                                   dark_image=Image.open("stock-removebg-preview.png"),
                                   size=(40, 40))
Srch = customtkinter.CTkButton(root, text="Search", command=search, image=srchimage, fg_color=buttoncolor, hover="disable",
                               width=150, corner_radius=10, border_width=2, border_color="black", border_spacing=2,
                               height=40)
Srch.place(x=1350, y=70)
saveButton = customtkinter.CTkButton(option_frame, text="Save", image=srchimage, fg_color=buttoncolor, hover="disable", width=150,
                                     corner_radius=10, border_width=2, border_color="black", border_spacing=2,
                                     height=40, command=Save)
saveButton.place(x=15, y=400)
customtkinter.CTkButton(option_frame, text="Reset", image=srchimage, fg_color=buttoncolor, hover="disable", width=150,
                        corner_radius=10, border_width=2, border_color="black", border_spacing=2, height=40,
                        command=Clear2).place(x=15, y=500)
customtkinter.CTkButton(option_frame, text="Exit", image=srchimage, fg_color=buttoncolor, hover="disable", width=150,
                        corner_radius=10, border_width=2, border_color="black", border_spacing=2, height=40,
                        command=Exit).place(x=15, y=600)



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


my_entry = Entry(obj2, font=("Helvetica", 20))
my_entry.place(x=10, y=10)

my_list = Listbox(obj2, width=50)
my_list.place(x=10, y=50)



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
