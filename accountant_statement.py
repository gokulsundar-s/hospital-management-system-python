from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
from datetime import datetime
from datetime import date
from decimal import *
import csv

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="hms")
cursor=mycon.cursor()

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("HOSPITAL MANAGEMENT SYSTEM - ACCOUNTANT")

def save():
    en1 = str(d1.get())
    en2 = str(e1.get())
    
    if(en1=="" or en2==""):
        messagebox.showerror("ERROR", "SOME FIELDS ARE EMPTY..!")
    
    else:
        show = ("SELECT * FROM accounts where Date BETWEEN '{}' AND '{}'").format(en1,en2)
        cursor.execute(show)
        data=cursor.fetchall()
        
        with open("C:/Users/WELCOME/Downloads/statement.csv", 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["AMOUNT","PAYMENT TYPE","DESCRIPTION","DEBIT/CREDIT"])
            
            for i in list(data):
                csvwriter.writerow(list(i[0:4]))
        
        Label(tk,text="Statemet file have been saved at your downloads",font=("Archivo Expanded",15),bg="#F5F5F5",fg="green").place(x=450,y=580)

show1 = ("SELECT sum(Amount) from accounts where Debit_credit = 'DEBIT'")
cursor.execute(show1)
d1 = cursor.fetchall()
s1 = int(d1[0][0])
    
show2 = ("SELECT SUM(Amount) from accounts where Debit_credit = 'CREDIT'")
cursor.execute(show2)
d2 = cursor.fetchall()
s2 = int(d2[0][0])

amt = s1+s2

a = Label(tk,text="Hospital  Management  System - Accountant",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
b = Label(tk,text="BALANCE AMOUNT:          "+str(amt),font=("Archivo Expanded",20),bg="#F6F6F6",fg="#1A374D").place(x=450,y=120)
c = Label(tk,text="TO DOWNLOAD STATEMENT",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=550,y=260)
d = Label(tk,text="FROM DATE:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=450,y=330)
d1=Entry(tk,font=("Archivo Expanded",13))
e = Label(tk,text="FROM DATE:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=450,y=400)
e1=Entry(tk,font=("Archivo Expanded",13))

btn=Button(tk,text="SAVE",font=("Archivo Expanded",12),bg="#1A374D",fg="#F6F6F6",command=save).place(x=680,y=480)

d1.place(x=750,y=330)
e1.place(x=750,y=400)


tk.mainloop()
