from tkinter import *
from tkinter import ttk
from tkinter import font


clicks = 0

def chek_click():
    global clicks
    label.config(text=clicks)
    clicks += 1
    return clicks





root = Tk()
root.title('clicker')
root.geometry('350x120')



label = ttk.Label(root, font='Arial 20', text=clicks)
label.pack(pady=20)

butn = ttk.Button(root, text='CLICK', command=chek_click)
butn.pack()





root.resizable(width=False, height=False)

root.mainloop()

