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

def save():
    en1 = str(b1.get())
    en2 = str(c1.get())
    en3 = str(d1.get())
    en4 = str(e1.get())

    show = ("SELECT Password FROM users where User_ID = '{}'").format(en1)
    cursor.execute(show)
    data=cursor.fetchall()

    if(len(data)<=0):
        messagebox.showerror("ERROR", "INVALID PASSWORD..!")
    else:
        if(en3!=en4):
            messagebox.showerror("ERROR", "PASSWORDS DOESNOT MATCH..!")
        elif(en3==en4 and len(en3)<8):
            messagebox.showerror("ERROR", "PASSWORD IS TOO WEAK..!")
        else:
            update = ("UPDATE users SET Password = '{}' where User_ID = '{}'").format(en3,en1)
            cursor.execute(update)
            mycon.commit()

            Label(tk,text="Password updated successfully..!",font=("Ailerons",25),bg="#F5F5F5",fg="Green").place(x=400,y=580)
            
            
a = Label(tk,text="Hospital  Management  System - PASSWORD",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

b=Label(tk,text="USER - ID: ",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=190)
b1=Entry(tk,font=("Archivo Expanded",13))
c=Label(tk,text="CURRENT PASSWORD: ",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=260)
c1=Entry(tk,font=("Archivo Expanded",13),show="*")
d=Label(tk,text="NEW PASSWORD: ",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=330)
d1=Entry(tk,font=("Archivo Expanded",13),show="*")
e=Label(tk,text="RE-ENTER NEW PASSWORD: ",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=400)
e1=Entry(tk,font=("Archivo Expanded",13),show="*")

bt3 = Button(tk,text="UPDATE",font=("Archivo Expanded",13),bg="#1A374D",fg="#F5F5F5",command=save).place(x=630,y=500)

b1.place(x=800,y=190)
c1.place(x=800,y=260)
d1.place(x=800,y=330)
e1.place(x=800,y=400)
tk.mainloop()
