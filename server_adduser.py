from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
import random
import array


mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="hms")
cursor=mycon.cursor()

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F6F6F6")
tk.title("HOSPITAL MANAGEMENT SYSTEM - SERVER")

def save():
    en1 = str(b1.get())
    en2 = str(c1.get())
    en3 = str(d1.get())
    en4 = str(e1.get())
    en5 = str(f1.get())
    en6 = str(g1.get())
    
    show = ("SELECT First_Name,Last_Name,DOB,Phone_Number FROM users")
    cursor.execute(show)
    data=cursor.fetchall()
    
    c = 0
    
    for i in data:
        if(en1 in list(i) and en2 in list(i) and en3 in list(i) and en4 in list(i)):
            c = 1
    
    if(c==1):
        messagebox.showerror("ERROR", "USER DATA ALREADY EXISTS..!")
    
    elif(en3=="DOCTOR" and en4==""):
        messagebox.showerror("ERROR", "SPECIALIZATION IS REQUIRED...!")
    
    elif(en3!="DOCTOR" and en4!=""):
        messagebox.showerror("ERROR", "SPECIALIZATION IS NOT REQUIRED..!")
    
    elif(en1=="" or en2=="" or en3=="" or en5=="" or en6==""):
        messagebox.showerror("ERROR", "SOME FIELDS ARE EMPTY..!")
    
    elif(len(en6)!=10 or not en6.isdigit()):
        messagebox.showerror("ERROR", "INVALID PHONE NUMBER..!")
        
    else:
        show=("SELECT User_ID from users WHERE Emp_type='{}'").format(en3)
        cursor.execute(show)
        data=cursor.fetchall()
    
        uid = en3[0:3]+"0"+str(len(data)+1)
    
        MAX_LEN = 8
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        SYMBOLS = ['@', '#', '$', '%', '=', '?', '/', '|','*', '(', ')']
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
        password = ""
        
        for x in temp_pass_list:
            password = password + x
    
        insert = ("insert into users values('{}','{}','{}','{}','{}','{}','{}','{}')").format(en1,en2,uid,en3,en5,en6,password,en4)
        cursor.execute(insert)
        mycon.commit()
        
        Label(tk,text="USER-ID:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=580,y=600)
        Label(tk,text=uid,font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=750,y=600)
        Label(tk,text="PASSWORD:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=580,y=680)
        Label(tk,text=password,font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=750,y=680)
        Label(tk,text="USER ADDED SUCCESSFULLY..!",font=("Archivo Expanded",15),bg="#F6F6F6",fg="green").place(x=520,y=750)

def back():
    tk.destroy()
    import server
        
a = Label(tk,text="Hospital  Management  System - Server",font=("Ailerons",40),bg="#F6F6F6",fg="#1A374D").pack()

b=Label(tk,text="FIRST-NAME:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=120)
b1=Entry(tk,font=("Archivo Expanded",13))
c=Label(tk,text="LAST-NAME:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=190)
c1=Entry(tk,font=("Archivo Expanded",13))
d=Label(tk,text="EMPLOYEE TYPE:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=260)
d1=ttk.Combobox(tk,font=("Archivo Expanded",13),width=19)
d1["values"]=("DOCTOR","NURSE","RECEPTIONIST","ACCOUNTANT")
e=Label(tk,text="SPECIALIZATION (if doctor only)",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=330)
e1=Entry(tk,font=("Archivo Expanded",13))
f=Label(tk,text="DATE OF BIRTH:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=400)
f1=Entry(tk,font=("Archivo Expanded",13))
g=Label(tk,text="PHONE NO.:",font=("Archivo Expanded",15),bg="#F6F6F6",fg="#1A374D").place(x=400,y=470)
g1=Entry(tk,font=("Archivo Expanded",13))
h=Button(tk,text="SUBMIT",font=("Archivo Expanded",12),bg="#1A374D",fg="#F6F6F6",command=save).place(x=650,y=550)
btb = Button(tk,text="<BACK",font=("Archivo Expanded",8),bg="#1A374D",fg="#F5F5F5",command=back).place(x=10,y=10)

b1.place(x=800,y=120)
c1.place(x=800,y=190)
d1.place(x=800,y=260)
e1.place(x=800,y=330)
f1.place(x=800,y=400)
g1.place(x=800,y=470)
tk.mainloop()

