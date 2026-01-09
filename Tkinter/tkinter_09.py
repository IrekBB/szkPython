# Images
"""
Etykiety (labels) i przyciski (buttons) mogą wyświetlać obrazki
W tkinterze możemy wyświetlać obrazki jedynie z rozszerzeniem gif

pip3.9.exe install Pillow

"""

from tkinter import *

# pip install pillow
from PIL import Image, ImageTk



root = Tk()

load = Image.open("M85M.gif")
render = ImageTk.PhotoImage(load)
img= Label(image=render)
img.image = render
img.place(x=0, y=0)

root.geometry("200x120")
root.mainloop()


"""
from tkinter import *

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("M85M.gif")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x120")
root.mainloop()
"""

