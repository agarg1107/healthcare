from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk,THEMES

def change_theme(theme,e=None):
    try:
        root.set_theme(theme)
    except:
        pass
#root = Tk()
root = ThemedTk(themebg=True)
root.set_theme('blue')
root.wm_minsize(width=500,height=300)
root.title("Tkinter Theme Example")
root.state('zoomed')

#----------------------------------------------------
exitImg = PhotoImage(file='icons/Exit.png')
newImg = PhotoImage(file='icons/mike_.png')
saveImg = PhotoImage(file='icons/pdf.png')
helpImg = PhotoImage(file='icons/about.png')
mainmenu = Menu(root,tearoff=0)
    
firstMenu = Menu(mainmenu, tearoff=0)
firstMenu.add_command(label="New",image=newImg,compound=LEFT,accelerator='Ctrl+N')
firstMenu.add_command(label="Save",image=saveImg,compound=LEFT,accelerator='Ctrl+P')
firstMenu.add_separator()


mainmenu.add_cascade(label="File", menu=firstMenu)
mainmenu.add_cascade(label="Help")
root.config(menu=mainmenu)
tc  = ttk.Combobox(root,values=THEMES)
tc.pack(anchor=SW,side=LEFT)
tc.set("Change theme")
tc.bind("<<ComboboxSelected>>",lambda e:change_theme(tc.get()))

#------------ adding some widgets to see theme effects---------------
l1 = ttk.Label(text="Label 1",width=15,font=15).pack(side=TOP,anchor=SW)
l2 = ttk.Label(text="Label 2",width=15,font=15).pack(side=TOP,anchor=SW,pady=20)
l3 = ttk.Label(text="Label 3",width=15,font=15).pack(side=TOP,anchor=SW)

b1 = ttk.Button(text="Button 1",width=15,style='C.TButton').pack(side=TOP,anchor=SW,pady=20)
b2 = ttk.Button(text="Button 2",width=15).pack(side=TOP,anchor=SW)
b3 = ttk.Button(text="Button 3",width=15).pack(side=TOP,anchor=SW,pady=20)
# ---------- adding a frame --------------
f1 = ttk.Frame(width=300,height=20)
tb = Text(f1,fg='blue',font=15,height=20).pack()
f1.pack(side=TOP,anchor=SW)
root.mainloop()
