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
tk.title("HOSPITAL MANAGEMENT SYSTEM")

def add():
    import accountant_add_income

def expence():
    import accountant_add_expanse

def statement():
    import accountant_statement

# def cpassword():
#     import mainpage_change_password

a = Label(tk,text="Hospital  Management  System - Accountant",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt1 = Button(tk,text="ADD INCOME",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=20,command=add).pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt2 = Button(tk,text="ADD EXPENCE",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=20,command=expence).pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt3 = Button(tk,text="SALARY",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=20).pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

bt4 = Button(tk,text="SEE STATEMENT",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=20,command=statement).pack()

# btn = Button(tk,text="CHANGE PASSWORD",font=("Archivo Expanded",10),bg="#1A374D",fg="#F5F5F5",command=cpassword).place(x=1200,y=100)

tk.mainloop()

tk.mainloop()
