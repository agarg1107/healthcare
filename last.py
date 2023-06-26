from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

import datetime
 # year, month, day

root = tk.Tk()

def get_d():
    diff21 = (d2 - d1).days

ttk.Label(root, text='Choose date').pack(padx=10, pady=10)

cal = DateEntry(root, width=12, background='red',
                    foreground='white', borderwidth=2, year=2023)
cal.pack(padx=10, pady=10)
selected_date = cal.get_date()
year = selected_date.year
month = selected_date.month
day = selected_date.day
d1 = datetime.date(year,month,day)
d2 = datetime.date(2023, 6, 27)
diff21 = (d2-d1).days
print(diff21)
print(str(cal.get()))




root.mainloop()
