from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk, THEMES
from tkinter import messagebox
import customtkinter
import sys
with open('necessaries/help.txt','r') as helpfile:
    lines= helpfile.readlines()
    help =''
    help = help.join(line for line in lines)



def helpWin(root,e=None):
        infowin = Toplevel(root)
        infowin.grab_set()
        #infowin.grab_release()
        infowin.title('Error')
        infowin.geometry("440x210+255+190")
        infowin.config(bg="black")

        infowin.resizable(0,0)
        aboutImg = PhotoImage(file='icons/about.png')
        conImg = PhotoImage(file='icons/tick.png')
        infowin.tk.call('wm', 'iconphoto', infowin._w, aboutImg)
        lbl = customtkinter.CTkLabel(infowin, text="Please Enter Mobile number", font=('Dotum', 18),
                    )
        lbl.place(x=100, y=20)
        ###
        okBtn = ttk.Button(infowin,text="  Quit  ",image=conImg,compound=LEFT,
                    style='C.TButton',cursor="hand2",command=infowin.destroy)
        okBtn.pack(side=TOP,pady=3)
        ###

        infowin.mainloop()
