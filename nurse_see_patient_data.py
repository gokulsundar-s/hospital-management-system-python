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

def check():
    en1 = str(b1.get())
    
    show = ("SELECT P_Name,DOB,Age,Gender,Blood_group,Height,Weight,Mail_ID,Phone_Number from patient where P_ID='{}'").format(en1)
    cursor.execute(show)
    data=cursor.fetchall()
    
    if(len(data)>0):     
        c1.insert(0,data[0][0])
        d1.insert(0,data[0][1])
        e1.insert(0,data[0][2])
        f1.insert(0,data[0][3])
        g1.insert(0,data[0][4])
        h1.insert(0,data[0][5])
        i1.insert(0,data[0][6])
        j1.insert(0,data[0][7])
        k1.insert(0,data[0][8])
            
    else:
        messagebox.showerror("ERROR", "USER DOESN'T EXISTS..!")


def back():
    tk.destroy()
    import mainpage_reception
a = Label(tk,text="Hospital  Management  System - Reception",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

b=Label(tk,text="PATIENTS ID:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=120)
b1=Entry(tk,font=("Archivo Expanded",13))
c=Label(tk,text="PATIENTS NAME:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=210)
c1=Entry(tk,font=("Archivo Expanded",13))
d=Label(tk,text="DATE OF BIRTH:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=280)
d1=Entry(tk,font=("Archivo Expanded",13))
e=Label(tk,text="AGE:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=350)
e1=Entry(tk,font=("Archivo Expanded",13),width=7)
f=Label(tk,text="GENDER:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=700,y=350)
f1=ttk.Combobox(tk,font=("Archivo Expanded",13),width=10)
f1["values"]=("MALE","FEMALE","OTHERS")
g=Label(tk,text="BLOOD GROUP:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=420)
g1=ttk.Combobox(tk,font=("Archivo Expanded",13),width=18)
g1["values"]=("B+ve","B-ve","O+ve","O-ve","AB+ve","A1+ve","A1-ve","A1B+ve","A1B-ve")
h=Label(tk,text="HEIGHT:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=490)
h1=Entry(tk,font=("Archivo Expanded",13),width=7)
i=Label(tk,text="WEIGHT:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=700,y=490)
i1=Entry(tk,font=("Archivo Expanded",13),width=7)
j=Label(tk,text="EMAIL:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=560)
j1=Entry(tk,font=("Archivo Expanded",13))
k=Label(tk,text="PHONE NUMBER:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=450,y=630)
k1=Entry(tk,font=("Archivo Expanded",13))

l=Button(tk,text="SUBMIT",font=("Archivo Expanded",10),bg="#1A374D",fg="#F6F6F6",command=check).place(x=1050,y=117)
btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)

b1.place(x=750,y=120)
c1.place(x=750,y=210)
d1.place(x=750,y=270)
e1.place(x=570,y=350)
f1.place(x=860,y=350)
g1.place(x=750,y=420)
h1.place(x=570,y=490)
i1.place(x=860,y=490)
j1.place(x=750,y=560)
k1.place(x=750,y=630)

tk.mainloop()

tk.mainloop()
