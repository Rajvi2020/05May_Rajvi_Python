import tkinter

tk = tkinter.Tk()
tk.title("My Playlist")
tk.geometry("400x400")
tk.config(background="lightblue")

b1 = tkinter.Button(text="Like", bg="lightblue", fg="red", font="Courier 15 bold")
b1.grid(row=0, column=0)

b2 = tkinter.Button(text="Share", bg="lightblue", fg="red", font="Courier 15 bold")
b2.grid(row=0, column=1)

b3 = tkinter.Button(text="Download", bg="lightblue", fg="red", font="Courier 15 bold")
b3.grid(row=1, column=0)

b4 = tkinter.Button(text="Add to Queue", bg="lightblue", fg="red", font="Courier 15 bold")
b4.grid(row=1, column=1)

tk.mainloop()