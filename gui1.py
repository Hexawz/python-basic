from tkinter import *
top = Tk()
top.geometry("400x800")
c = Canvas(top,bg = "red",height = "200",width = 200)
arc = c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")
c.pack()
top.mainloop()
