from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="hms")
cursor=mycon.cursor()

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F6F6F6")
tk.title("HOSPITAL MANAGEMENT SYSTEM - SERVER")

def check():
    en1 = str(b1.get())
    
    show = ("SELECT First_Name,Last_Name,Emp_type,DOB,Phone_Number FROM users where User_ID = '{}'").format(en1)
    cursor.execute(show)
    data=cursor.fetchall()
    
    if(len(data)>0):       
        c1.insert(0,data[0][0])
        d1.insert(0,data[0][1])
        e1.insert(0,data[0][2])
        f1.insert(0,data[0][3])
        h1.insert(0,data[0][4])
    
    else:
        messagebox.showerror("ERROR", "USER DOESN'T EXISTS..!")
        
def save():
    en1 = str(b1.get())
    en2 = str(c1.get())
    en3 = str(d1.get())
    en4 = str(e1.get())
    en5 = str(f1.get()) 
    en6 = str(h1.get()) 
    
    insert = ("UPDATE users SET First_Name = '{}',Last_Name = '{}',Emp_type = '{}',DOB = '{}',Phone_Number = '{}' WHERE User_ID='{}'").format(en2,en3,en4,en5,en6,en1)
    cursor.execute(insert)
    mycon.commit()
    
    Label(tk,text="USER DATA UPDATED SUCCESSFULLY..!",font=("Archivo Expanded",15),bg="#F6F6F6",fg="green").place(x=520,y=700)

def back():
    tk.destroy()
    import server

a = Label(tk,text="Hospital  Management  System - Server",font=("Ailerons",40),bg="#F6F6F6",fg="#1A374D").pack()

b=Label(tk,text="USER ID:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=120)
b1=Entry(tk,font=("Archivo Expanded",13))
b11=Label(tk,text="EDIT THE USER DETAILS BELOW",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=540,y=190)
c=Label(tk,text="FIRST-NAME:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=260)
c1=Entry(tk,font=("Archivo Expanded",13))
d=Label(tk,text="LAST-NAME:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=330)
d1=Entry(tk,font=("Archivo Expanded",13))
e=Label(tk,text="EMPLOYEE TYPE:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=400)
e1=ttk.Combobox(tk,font=("Archivo Expanded",13),width=19)
e1["values"]=("DOCTOR","NURSE","PHARMACY","TECHNICIANS","RECEPTIONIST","SECURITY")
f=Label(tk,text="DATE OF BIRTH",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=470)
f1=Entry(tk,font=("Archivo Expanded",13))
g=Label(tk,text="PHONE NO.:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=490,y=540)
h1=Entry(tk,font=("Archivo Expanded",13))

i=Button(tk,text="SUBMIT",font=("Archivo Expanded",12),bg="#1A374D",fg="#F6F6F6",command=check).place(x=1050,y=110)
h=Button(tk,text="UPDATE",font=("Archivo Expanded",12),bg="#1A374D",fg="#F6F6F6",command=save).place(x=650,y=610)
btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)



b1.place(x=750,y=120)
c1.place(x=750,y=260)
d1.place(x=750,y=330)
e1.place(x=750,y=400)
f1.place(x=750,y=470)
h1.place(x=750,y=540)
tk.mainloop()

