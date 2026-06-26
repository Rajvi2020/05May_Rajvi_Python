import tkinter
import pymysql
import re
from tkinter import messagebox,ttk
tk=tkinter.Tk()
tk.title("tkinterdatabase")
tk.geometry("400x400")
tk.config(background="lightblue")

l1=tkinter.Label(text="Name:",bg="lightblue",fg="red",font='Courier 15 bold')
l1.grid(row=0,column=0,sticky='w')


l2=tkinter.Label(text="Email:",bg="lightblue",fg="red",font='Courier 15 bold')
l2.grid(row=1,column=0,sticky='w')

l3=tkinter.Label(text="Mobile:",bg="lightblue",fg="red",font='Courier 15 bold')
l3.grid(row=2,column=0,sticky='w')

t1=tkinter.Entry()
t1.grid(row=0,column=1,sticky='w')

t2=tkinter.Entry()
t2.grid(row=1,column=1,sticky='w')

t3=tkinter.Entry()
t3.grid(row=2,column=1,sticky='w')


try:
  db=pymysql.connect(host='localhost',user='root',password='',database='tkinter_database')
  print("database connected")
except Exception as e:
  print(e)


cr=db.cursor()
"""tab_create="create table t_data (name varchar(20),email varchar(100),mobile varchar(20))"
try:
  cr.execute(tab_create)
  db.commit()
except Exception as e:
  print(e)"""

def buttonclick():
    name = t1.get().strip()
    email = t2.get().strip()
    mobile = t3.get().strip()

    # Empty Validation
    if name == "" or email == "" or mobile == "":
        messagebox.showwarning("Warning", "All fields are required!")
        return

    # Name Validation
    if not name.replace(" ", "").isalpha():
        messagebox.showwarning("Warning", "Name should contain only alphabets.")
        return

    # Email Validation
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'

    if not re.match(pattern, email):
        messagebox.showwarning("Warning", "Enter valid Gmail address.")
        return

    # Mobile Validation
    if not mobile.isdigit():
        messagebox.showwarning("Warning", "Mobile number must contain only digits.")
        return

    if len(mobile) != 10:
        messagebox.showwarning("Warning", "Mobile number must be exactly 10 digits.")
        return

    # Database Insert
    sql = "insert into t_data(name,email,mobile) values(%s,%s,%s)"
    val = (name, email, mobile)

    try:
        cr.execute(sql, val)
        db.commit()

        # Success Message
        messagebox.showinfo(
            "Data Saved",
            f"Record Inserted Successfully\n\n"
            f"Name : {name}\n"
            f"Email : {email}\n"
            f"Mobile : {mobile}"
        )

        # Clear Entry Boxes
        t1.delete(0, tkinter.END)
        t2.delete(0, tkinter.END)
        t3.delete(0, tkinter.END)

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

  
btn = tkinter.Button(text="Submit",command=buttonclick,bg="lightblue",fg="red",font="Courier 15 bold")
btn.place(x=150, y=250)

sec_data="select * from t_data"
try:
  cr.execute(sec_data)
  db.commit()
  data=cr.fetchall()
  print(data)
except Exception as e:
  print(e) 
 

tk.mainloop()

db.close()