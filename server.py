from tkinter import *
from tkinter import ttk
import mysql.connector as sql

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="hms")
cursor=mycon.cursor()

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("HOSPITAL MANAGEMENT SYSTEM - SERVER")

def newuser():
    tk.destroy()
    import server_adduser

def delete():
    tk.destroy()
    import server_delete

def edit():
    tk.destroy()
    import server_edituser

def report():
    tk.destroy()
    import server_report  

def back():
    tk.destroy()
    import mainpage 
    
a = Label(tk,text="Hospital  Management  System - Server",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt1 = Button(tk,text="ADD USERS",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=15,command=newuser).pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt2 = Button(tk,text="EDIT USER",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=15,command=edit).pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt3 = Button(tk,text="DELETE USER",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=15,command=delete).pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt4 = Button(tk,text="USER REPORT",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=15,command=report).pack()
btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)
tk.mainloop()

