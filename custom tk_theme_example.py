from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk,THEMES
import dialogbox

def change_theme(theme,e=None):
    try:
        root.set_theme(theme)
    except:
        pass
#root = Tk()
root = ThemedTk(themebg=True)
##root.set_theme('blue')
root.wm_minsize(width=600,height=300)
root.title("Tkinter Theme Example")
root.state('zoomed')
logoImg = PhotoImage(file='icons/logo1.png')
root.tk.call('wm', 'iconphoto', root._w, logoImg)

style = ttk.Style()

style.map("TButton",
          foreground=[('pressed','brown'),('active','green')],
          background =[('pressed','black'),('active','sky blue')])
style.configure("TButton",width=20,font=('arial',15,'bold'),foreground='red',relief='sunken')
style.configure("TLabel",foreground='white',background='steel blue')
style.configure("C.TLabel",foreground='white',background='black')

#----------------------------------------------------
exitImg = PhotoImage(file='icons/Exit.png')
newImg = PhotoImage(file='icons/mike_.png')
saveImg = PhotoImage(file='icons/pdf.png')
helpImg = PhotoImage(file='icons/about.png')
mainmenu = Menu(root,tearoff=0)
    
firstMenu = Menu(mainmenu, tearoff=0)
firstMenu.add_command(label="New",image=newImg,compound=LEFT,accelerator='Ctrl+N')
firstMenu.add_command(label="Save",image=saveImg,compound=LEFT,accelerator='Ctrl+S')
firstMenu.add_separator()


mainmenu.add_cascade(label="File", menu=firstMenu)
mainmenu.add_cascade(label="Help",command=lambda:dialogbox.helpWin(root))
root.config(menu=mainmenu)

#------------ adding some widgets to see theme effects---------------
l1 = Label(text="Custom Dialog Box Example [Tkinter]",font=('arial',25),bg='steel blue')
l1.pack(side=TOP,anchor=N,fill=X)
l2 = ttk.Label(text="Label 2",width=15,font=15).pack(side=TOP,anchor=SW,pady=20,padx=10)
l3 = ttk.Label(text="Label 3",width=15,font=15).pack(side=TOP,anchor=SW,padx=10)

b1 = ttk.Button(text="Button 1",width=15).pack(side=TOP,anchor=SW,pady=20,padx=10)
b2 = ttk.Button(text="Button 2",width=15).pack(side=TOP,anchor=SW,padx=10)
b3 = ttk.Button(text="Button 3",width=15).pack(side=TOP,anchor=SW,pady=20,padx=10)
# ---------- adding a frame --------------
f1 = ttk.Frame(width=200)
tb = Text(f1,fg='blue',font=15,height=15).pack()
f1.pack(side=TOP,anchor=SW,padx=10)

tc  = ttk.Combobox(root,values=THEMES)
tc.pack(anchor=SW,side=BOTTOM,padx=10)
tc.set("Change theme")
tc.bind("<<ComboboxSelected>>",lambda e:change_theme(tc.get()))

root.mainloop()
