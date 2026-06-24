import tkinter
import pymysql
import re
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
  name=t1.get()
  email=t2.get()
  mobile=t3.get()
  sql="insert into t_data(name,email,mobile) values(%s, %s, %s)"
  val=(name,email,mobile)
  try:
    cr.execute(sql,val)
    db.commit()
  except Exception as e:
    print(e)

btn = tkinter.Button(text="Submit",command=buttonclick,bg="lightblue",fg="red",font="Courier 15 bold")
btn.place(x=150, y=250)

tk.mainloop()

db.close()