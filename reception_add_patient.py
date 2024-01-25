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
tk.title("HOSPITAL MANAGEMENT SYSTEM - RECEPTION")

def save():
    en1 = str(b1.get())
    en2 = str(c1.get())
    en3 = d1.get()
    en4 = str(e1.get())
    en5 = str(f1.get())
    en6 = str(g1.get())
    en7 = str(h1.get())
    en8 = str(i1.get())
    en9 = str(j1.get())
    
    show = ("SELECT * FROM patient where P_Name='{}' and Phone_Number='{}'").format(en1,en9)
    cursor.execute(show)
    data=cursor.fetchall()
    
    if(len(data)>0):
        messagebox.showerror("ERROR", "USER DATA ALREADY EXISTS..!")
    
    elif(en1=="" or en2=="" or en3=="" or en4=="" or en5=="" or en6=="" or en7=="" or en8=="" or en9==""):
        messagebox.showerror("ERROR", "SOME FIELDS ARE EMPTY..!")
    
    else:
        show=("SELECT * from patient")
        cursor.execute(show)
        data=cursor.fetchall()
    
        pid = "PID0"+str(len(data)+1)
        
        insert = ("insert into patient values('{}','{}','{}',{},'{}','{}','{}','{}','{}','{}')").format(pid,en1,en2,en3,en4,en5,en6,en7,en8,en9)
        cursor.execute(insert)
        mycon.commit()
        
        Label(tk,text="USER-ID:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=580,y=700)
        Label(tk,text=pid,font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=750,y=700)
        Label(tk,text="PATIENT ADDED SUCCESSFULLY..!",font=("Archivo Expanded",15),bg="#F6F6F6",fg="green").place(x=520,y=750)

def back():
    tk.destroy()
    import mainpage_reception
    
a = Label(tk,text="Hospital  Management  System - Reception",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

b=Label(tk,text="PATIENTS NAME:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=120)
b1=Entry(tk,font=("Archivo Expanded",13))
c=Label(tk,text="DATE OF BIRTH:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=190)
c1=Entry(tk,font=("Archivo Expanded",13))
d=Label(tk,text="AGE:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=260)
d1=Entry(tk,font=("Archivo Expanded",13),width=7)
e=Label(tk,text="GENDER:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=700,y=260)
e1=ttk.Combobox(tk,font=("Archivo Expanded",13),width=10)
e1["values"]=("MALE","FEMALE","OTHERS")
f=Label(tk,text="BLOOD GROUP:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=330)
f1=ttk.Combobox(tk,font=("Archivo Expanded",13),width=18)
f1["values"]=("B+ve","B-ve","O+ve","O-ve","AB+ve","A1+ve","A1-ve","A1B+ve","A1B-ve")
g=Label(tk,text="HEIGHT:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=400)
g1=Entry(tk,font=("Archivo Expanded",13),width=7)
h=Label(tk,text="WEIGHT:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=700,y=400)
h1=Entry(tk,font=("Archivo Expanded",13),width=7)
i=Label(tk,text="EMAIL:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=470)
i1=Entry(tk,font=("Archivo Expanded",13))
j=Label(tk,text="PHONE NUMBER:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=540)
j1=Entry(tk,font=("Archivo Expanded",13))

j=Button(tk,text="SUBMIT",font=("Archivo Expanded",13),bg="#1A374D",fg="#F5F5F5",command=save).place(x=650,y=620)
btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)

b1.place(x=750,y=120)
c1.place(x=750,y=190)
d1.place(x=580,y=260)
e1.place(x=860,y=260)
f1.place(x=750,y=330)
g1.place(x=580,y=400)
h1.place(x=860,y=400)
i1.place(x=750,y=470)
j1.place(x=750,y=540)

tk.mainloop()
