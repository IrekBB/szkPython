# Canvas

"""
# Program 1

import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
top.mainloop()
"""

# Program 2
import tkinter
root = tkinter.Tk()

canvas = tkinter.Canvas (width=200, height=200, bg='white')
canvas.create_rectangle(20, 100, 30,150,fill='red')
canvas.create_oval (20,100,70,180, fill='blue')
canvas.create_line (20,100,70,180, fill='green')

canvas.pack()
root.mainloop()
