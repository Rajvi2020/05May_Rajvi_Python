import tkinter

tk = tkinter.Tk()
tk.title("Calculator")
tk.geometry("400x400")
tk.config(background="lightblue")

l1 = tkinter.Label(text="First Number", bg="lightblue", fg="red", font="Courier 15 bold")
l1.grid(row=0, column=0, sticky="w")

l2 = tkinter.Label(text="Second Number", bg="lightblue", fg="red", font="Courier 15 bold")
l2.grid(row=1, column=0, sticky="w")

t1 = tkinter.Entry()
t1.grid(row=0, column=1)

t2 = tkinter.Entry()
t2.grid(row=1, column=1)

l3 = tkinter.Label(text="", bg="lightblue", fg="blue", font="Courier 15 bold")
l3.grid(row=4, column=0, columnspan=2)

def add():
    ans = int(t1.get()) + int(t2.get() )
    l3.config(text="Result = " + str(ans))

def sub():
    ans = int(t1.get()) - int(t2.get())
    l3.config(text="Result = " + str(ans))

def mul():
    ans = int(t1.get()) * int(t2.get())
    l3.config(text="Result = " + str(ans))

def div():
    ans = int(t1.get()) / int(t2.get())
    l3.config(text="Result = " + str(ans))

b1 = tkinter.Button(text="+", command=add)
b1.grid(row=2, column=0)

b2 = tkinter.Button(text="-", command=sub)
b2.grid(row=2, column=1)

b3 = tkinter.Button(text="*", command=mul)
b3.grid(row=3, column=0)

b4 = tkinter.Button(text="/", command=div)
b4.grid(row=3, column=1)

tk.mainloop()