import tkinter

tk = tkinter.Tk()
tk.title("My Playlist")
tk.geometry("400x400")
tk.config(background="lightblue")

l1 = tkinter.Label(text="Welcome to Your Music Playlist",
                   bg="lightblue",
                   fg="red",
                   font="Courier 15 bold")
l1.grid(row=0, column=0, columnspan=3)

l2 = tkinter.Label(text="",
                   bg="lightblue",
                   fg="blue",
                   font="Courier 15 bold")
l2.grid(row=2, column=0, columnspan=3)

def play():
    l2.config(text="Playing")

def pause():
    l2.config(text="Paused")

def next():
    l2.config(text="Next Song")

b1 = tkinter.Button(text="Play", command=play)
b1.grid(row=1, column=0)

b2 = tkinter.Button(text="Pause", command=pause)
b2.grid(row=1, column=1)

b3 = tkinter.Button(text="Next", command=next)
b3.grid(row=1, column=2)

tk.mainloop()