from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
from datetime import datetime
from datetime import date

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="hms")
cursor=mycon.cursor()

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("HOSPITAL MANAGEMENT SYSTEM - RECEPTION")

def newdata():
    import reception_add_patient
    
def deletedata():
    import reception_delete_patient

def editdata():
    import reception_edit_patient

def appointment():
    import reception_book_appointment

def back():
    tk.destroy()
    import mainpage

a = Label(tk,text="Hospital  Management  System - Reception",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt1 = Button(tk,text="NEW PATIENT REGIATRATION",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=30,command=newdata).pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt2 = Button(tk,text="EDIT PATIENT DATA",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=30,command=editdata).pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt3 = Button(tk,text="DELETE PATIENT DATA",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=30,command=deletedata).pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt4 = Button(tk,text="BOOK APPOINTMENT",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=30,command=appointment).pack()
btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)

tk.mainloop()
