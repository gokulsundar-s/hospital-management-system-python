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
tk.title("HOSPITAL MANAGEMENT SYSTEM - ACCOUNTANT")

def save():
    en1 = b1.get()
    en2 = str(c1.get())
    en3 = str(d1.get())
    en4 = str(e1.get())
    
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    dte = date.today()
    
    if(str(en1)=="" or en2=="" or en3=="" or en4==""):
        messagebox.showerror("ERROR", "SOME FIELDS ARE EMPTY..!")
    
    elif(en4!="0102"):
        messagebox.showerror("ERROR", "WRONG T-PIN..!")
    
    elif(en4=="0102"):
        insert = ("INSERT INTO accounts VALUES({},'{}','{}','CREDIT','{}','{}')").format(en1,en2,en3,dte,ct)
        cursor.execute(insert)
        mycon.commit()
        
a = Label(tk,text="Hospital  Management  System - Accountant",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()

b=Label(tk,text="AMOUNT:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=120)
b1=Entry(tk,font=("Archivo Expanded",13))
c=Label(tk,text="PAYMENT TYPE:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=190)
c1=ttk.Combobox(tk,font=("Archivo Expanded",13),width=19)
c1["values"]=("CHECK","CASH","ACCOUNT TRANSFER","UPI")
d=Label(tk,text="DESCRIPTION:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=260)
d1=Entry(tk,font=("Archivo Expanded",13))
e = Label(tk,text="ENTER T-PIN:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=330)
e1 = Entry(tk,font=("Archivo Expanded",13),show="*")

g=Button(tk,text="SAVE",font=("Archivo Expanded",12),bg="#1A374D",fg="#F6F6F6",command=save).place(x=660,y=400)


b1.place(x=750,y=120)
c1.place(x=750,y=190)
d1.place(x=750,y=260)
e1.place(x=750,y=330)


tk.mainloop()
