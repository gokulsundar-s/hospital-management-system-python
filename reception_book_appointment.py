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
    en3 = str(d1.get())
    
    show = ("SELECT * FROM appointments where P_ID='{}' and Date='{}'").format(en1,en2)
    cursor.execute(show)
    data=cursor.fetchall()
    
    show1=("SELECT * from patient WHERE P_ID = '{}'").format(en1)
    cursor.execute(show1)
    data1=cursor.fetchall()
    
    c = 0
    
    for i in data:
        if(en1 in list(i) and en2 in list(i) and en3 in list(i)):
            c = 1
    
    if(len(data1)==0):
        messagebox.showerror("ERROR", "INVALID PATIENT DATA..!")
        
    elif(c==1):
        messagebox.showerror("ERROR", "APPOINTMENT ALREADY BOOKED..!")
    
    elif(en1=="" or en2=="" or en3==""):
        messagebox.showerror("ERROR", "SOME FIELDS ARE EMPTY..!")
        
    else:
        show=("SELECT * from appointments WHERE D_Name = '{}' and Date='{}'").format(en3,en2)
        cursor.execute(show)
        data=cursor.fetchall()
            
        ano = len(data)+1
        
        insert = ("insert into appointments values('{}','{}','{}',{})").format(en1,en3,en2,ano)
        cursor.execute(insert)
        mycon.commit()
        
        Label(tk,text="APPOINTMENT DATE:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=450,y=500)
        Label(tk,text=en2,font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=820,y=500)
        Label(tk,text="APPOINTMENT NUMBER:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=450,y=570)
        Label(tk,text=ano,font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=820,y=570)
        Label(tk,text="USER ADDED SUCCESSFULLY..!",font=("Archivo Expanded",15),bg="#F6F6F6",fg="green").place(x=520,y=620)

def back():
    tk.destroy()
    import mainpage_reception
    
a = Label(tk,text="Hospital  Management  System - Reception",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()

show1=("SELECT First_Name,D_spec from users WHERE Emp_type='DOCTOR'")
cursor.execute(show1)
dl=cursor.fetchall()

d_list = []
st = ""

for i in dl:
    st = i[0]+" - "+i[1]
    d_list.append(st)
    st = ""  
    
b=Label(tk,text="PATIENT ID:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=430,y=120)
b1=Entry(tk,font=("Archivo Expanded",13))
c=Label(tk,text="DATE OF APPOINTMENT:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=430,y=190)
c1=Entry(tk,font=("Archivo Expanded",13))
d=Label(tk,text="DOCTOR REFFERED:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=260)
d1=ttk.Combobox(tk,font=("Archivo Expanded",13),width=19)
d1["values"]=tuple(d_list)
e=Button(tk,text="SUBMIT",font=("Archivo Expanded",13),bg="#1A374D",fg="#F5F5F5",command=save).place(x=680,y=340)

btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)

b1.place(x=780,y=120)
c1.place(x=780,y=190)
d1.place(x=780,y=260)

tk.mainloop()
