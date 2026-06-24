import tkinter
import pymysql

tk = tkinter.Tk()
tk.title("Tkinter Database")
tk.geometry("400x400")
tk.config(background="lightblue")

l1 = tkinter.Label(text="Name:", bg="lightblue", fg="red", font="Courier 15 bold")
l1.grid(row=0, column=0)

l2 = tkinter.Label(text="Email:", bg="lightblue", fg="red", font="Courier 15 bold")
l2.grid(row=1, column=0)

l3 = tkinter.Label(text="Mobile:", bg="lightblue", fg="red", font="Courier 15 bold")
l3.grid(row=2, column=0)

t1 = tkinter.Entry()
t1.grid(row=0, column=1)

t2 = tkinter.Entry()
t2.grid(row=1, column=1)

t3 = tkinter.Entry()
t3.grid(row=2, column=1)


db = pymysql.connect(
    host="localhost",user="root",password="",database="tkinter_database")

cr = db.cursor()

# Create Table
"""try:
    cr.execute
    ("create table tkinterdata(name VARCHAR(20),email VARCHAR(100),mobile VARCHAR(20))")
    db.commit()
except Exception as e:
    print(e)"""

def btnClick():
    name = t1.get()
    email = t2.get()
    mobile = t3.get()

    sql = "insert into tkinterdata(name,email,mobile) VALUES(%s,%s,%s)"

    val = (name, email, mobile)

    try:
        cr.execute(sql, val)
        db.commit()
        print("Data Inserted Successfully")
    except Exception as e:
        print(e)

btn = tkinter.Button(
    text="Submit",
    command=btnClick,
    bg="lightblue",
    fg="red",
    font="Courier 15 bold"
)
btn.place(x=150, y=250)

tk.mainloop()

db.close()