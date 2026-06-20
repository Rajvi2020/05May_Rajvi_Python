import tkinter

tk = tkinter.Tk()
tk.title("Login Form")
tk.geometry("400x400")
tk.config(background="lightblue")

l1 = tkinter.Label(text="Username:", bg="lightblue", fg="red", font="Courier 15 bold")
l1.grid(row=0, column=0, sticky="w")

l2 = tkinter.Label(text="Password:", bg="lightblue", fg="red", font="Courier 15 bold")
l2.grid(row=1, column=0, sticky="w")

t1 = tkinter.Entry()
t1.grid(row=0, column=1)

t2 = tkinter.Entry(show="*")
t2.grid(row=1, column=1)

l3 = tkinter.Label(text="", bg="lightblue", fg="blue", font="Courier 15 bold")
l3.grid(row=3, column=0, columnspan=2)

def login():
    if t1.get() != "" and t2.get() != "":
        l3.config(text="Login Successful")

btn = tkinter.Button(text="Login", bg="lightblue", fg="red", font="Courier 15 bold", command=login)
btn.grid(row=2, column=0, columnspan=2)

tk.mainloop()