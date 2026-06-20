import tkinter
tk = tkinter.Tk()
tk.title("My Playlist")
tk.geometry("400x400")
tk.config(background="lightblue")

l1 = tkinter.Label(
    text="Welcome to Your Music Playlist",bg="lightblue",fg="red",font="Courier 15 bold")

l1.grid(row=0, column=0)

tk.mainloop()