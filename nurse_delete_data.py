from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
from datetime import datetime
from datetime import date

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="hms")
cursor=mycon.cursor()

tk=Tk()
tk.geometry("1915x1080")
tk.config(bg="#F5F5F5")
tk.title("HOSPITAL MANAGEMENT SYSTEM - NURSE")

def save():
    en1 = str(b1.get())
    
    show = ("SELECT * FROM patient where P_ID='{}'").format(en1)
    cursor.execute(show)
    data=cursor.fetchall()
        
    if(len(data)>0):
        inp = messagebox.askyesno("CONFIRM TO DELETE","ARE YOU SURE TO DELETE THE USER")
        
        if(inp==True):
            delete = ("DELETE FROM patient WHERE P_ID='{}'").format(en1)
            cursor.execute(delete)
            mycon.commit()
            Label(tk,text="USER DELETED SUCCESSFULLY..!",font=("Archivo Expanded",15),bg="#F6F6F6",fg="green").place(x=520,y=300)
    
    else:
        messagebox.showerror("ERROR", "USER DOESN'T EXISTS..!")

def back():
    tk.destroy()
    import mainpage_reception
     
a = Label(tk,text="Hospital  Management  System - NURSE",font=("Ailerons",40),bg="#F6F6F6",fg="#1A374D").pack()

b=Label(tk,text="PATEINT ID:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=190)
b1=Entry(tk,font=("Archivo Expanded",13))

c=Button(tk,text="SUBMIT",font=("Archivo Expanded",12),bg="#1A374D",fg="#F6F6F6",command=save).place(x=1050,y=180)
btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)

b1.place(x=700,y=190)
tk.mainloop()
