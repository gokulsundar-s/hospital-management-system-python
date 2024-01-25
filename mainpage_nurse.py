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
tk.title("HOSPITAL MANAGEMENT SYSTEM - NURSE")

def check():
    tk.destroy()
    import nurse_appointment

def back():
    tk.destroy()
    import mainpage
    
def seedata():
    tk.destroy()
    import nurse_see_patient_data

def delete():
    tk.destroy()
    import nurse_delete_data
    

a = Label(tk,text="Hospital  Management  System - Nurse",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()

bt1 = Button(tk,text="APPOINTMENTS",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=20,command=check).place(x=590,y=200)
bt2 = Button(tk,text="PATIENT DATA",font=("Archivo Expanded",18),bg="#1A374D",fg="#F5F5F5",height=2,width=20,command=seedata).place(x=590,y=450)

btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)

tk.mainloop()
