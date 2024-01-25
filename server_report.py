from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
import csv

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="hms")
cursor=mycon.cursor()

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F6F6F6")
tk.title("HOSPITAL MANAGEMENT SYSTEM - SERVER")

def save():
    en1 = str(b1.get())
    en2 = str(c1.get())
    
    if(en1=="" or en2==""):
        messagebox.showerror("ERROR", "SOME FIELDS ARE EMPTY..!")
    
    else:
        show = ("SELECT * FROM login where Date BETWEEN '{}' AND '{}'").format(en1,en2)
        cursor.execute(show)
        data=cursor.fetchall()
        
        with open("C:/Users/WELCOME/Downloads/user_report.csv", 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["USER ID","DATE","TIME"])
            
            for i in list(data):
                csvwriter.writerow(list(i))
        
        Label(tk,text="Report file have been saved at your downloads",font=("Archivo Expanded",15),bg="#F5F5F5",fg="green").place(x=470,y=400)

a = Label(tk,text="Hospital  Management  System - Server",font=("Ailerons",40),bg="#F6F6F6",fg="#1A374D").pack()
b = Label(tk,text="FROM DATE:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=450,y=120)
b1=Entry(tk,font=("Archivo Expanded",13))
c = Label(tk,text="FROM DATE:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=450,y=190)
c1=Entry(tk,font=("Archivo Expanded",13))

btn=Button(tk,text="SAVE",font=("Archivo Expanded",12),bg="#1A374D",fg="#F6F6F6",command=save).place(x=680,y=270)

b1.place(x=750,y=120)
c1.place(x=750,y=190)

tk.mainloop()
