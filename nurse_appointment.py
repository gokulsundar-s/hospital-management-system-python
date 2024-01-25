from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
from datetime import datetime
from datetime import date
import csv

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="hms")
cursor=mycon.cursor()

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("HOSPITAL MANAGEMENT SYSTEM - NURSE")

def save():
    en1=str(b1.get())
    en2=str(c1.get())
   
    if(en1=="" or en2==""):
        messagebox.showerror("ERROR", "SOME FIELDS ARE EMPTY..!")
    
    else:
        show = ("SELECT * FROM appointments where D_Name='{}' and Date='{}'").format(en1,en2)
        cursor.execute(show)
        data=cursor.fetchall()
        
        with open("C:/Users/WELCOME/Downloads/appiontment.csv", 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["P_ID","D_NAME","DATE","APPOINTMENT NUMBER"])
            
            for i in list(data):
                csvwriter.writerow(i)
        
        Label(tk,text="Appointment file have been saved at your downloads",font=("Archivo Expanded",15),bg="#F5F5F5",fg="green").place(x=450,y=400)
        
def back():
    tk.destroy()
    import mainpage_nurse
    
a = Label(tk,text="Hospital  Management  System - Nurse",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
Label(tk,text="\n",bg="#F5F5F5",fg="#1A374D").pack()
b=Label(tk,text="DOCTOR NAME:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=420,y=120)
b1=Entry(tk,font=("Archivo Expanded",13))
c=Label(tk,text="DATE OF APPOINTMENT:",font=("Archivo Expanded",15),bg="#F5F5F5",fg="#1A374D").place(x=420,y=190)
c1=Entry(tk,font=("Archivo Expanded",13))

bt=Button(tk,text="SUBMIT",font=("Archivo Expanded",13),bg="#1A374D",fg="#F5F5F5",command=save).place(x=650,y=250)
btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)

b1.place(x=770,y=120)
c1.place(x=770,y=190)

tk.mainloop()
