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
tk.title("HOSPITAL MANAGEMENT SYSTEM")

def login():
    en1=str(c1.get())
    en2=str(d1.get())
    
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    dte = date.today()

    if(en1=="admin" and en2=="Admin@123"):
        tk.destroy()
        import server
        insert = ("insert into login values('{}','{}','{}')").format(en1,dte,ct)
        cursor.execute(insert)
        mycon.commit()
        
    else:
        show=("Select * from users where User_ID='{}' and Password='{}'").format(en1,en2)
        cursor.execute(show)
        data=cursor.fetchall()
        mycon.commit()

        if(len(data)>0):
            insert = ("insert into login values('{}','{}','{}')").format(en1,dte,ct)
            cursor.execute(insert)
            mycon.commit()
                        
            if("ACC" in data[0][2]):
                tk.destroy()
                import mainpage_accounts
            
            elif("REC" in data[0][2]):
                tk.destroy()
                import mainpage_reception
                
            elif("NUR" in data[0][2]):
                tk.destroy()   
                import mainpage_nurse

        else:
            messagebox.showerror("ERROR", "INVALID USER-ID OR PASSWORD..!")

a = Label(tk,text="Hospital  Management  System",font=("Ailerons",40),bg="#F5F5F5",fg="#1A374D").pack()
b = Label(tk,text="\nLOGIN",font=("Archivo SemiCondensed Black",30),bg="#F5F5F5",fg="#1A374D").pack()
c = Label(tk,text="\nUSER-ID",font=("Archivo Expanded",20),bg="#F5F5F5",fg="#1A374D").pack()
c1 = Entry(tk,font=("Calibri",18))
c1.pack()
d = Label(tk,text="\nPASSWORD",font=("Archivo Expanded",20),bg="#F5F5F5",fg="#1A374D").pack()
d1 = Entry(tk,font=("Calibri",18),show="*")
d1.pack()
Label(tk,text="\n").pack()
bt1 = Button(tk,text="LOGIN",font=("Archivo Expanded",15),bg="#1A374D",fg="#F5F5F5",command=login).pack()

tk.mainloop()
